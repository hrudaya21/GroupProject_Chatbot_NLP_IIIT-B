from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
# Import smtplib for the email sending function
import smtplib
import email
from email.mime.text import MIMEText

import traceback

# Action class to verify the location to see if the user entered location is a supported city.
# We also check for spelling mistakes by the customer by considering edits at a distance of one and two from
# the correct name of the city.
class ActionVerifyLocation(Action):
	def edits_one(self,word):
	    "Create all edits that are one edit away from `word`."
	    alphabets    = 'abcdefghijklmnopqrstuvwxyz'
	    splits     = [(word[:i], word[i:])                   for i in range(len(word) + 1)]
	    deletes    = [left + right[1:]                       for left, right in splits if right]
	    inserts    = [left + c + right                       for left, right in splits for c in alphabets]
	    replaces   = [left + c + right[1:]                   for left, right in splits if right for c in alphabets]
	    transposes = [left + right[1] + right[0] + right[2:] for left, right in splits if len(right)>1]
	    return set(deletes + inserts + replaces + transposes)

	def edits_two(self,word):
	    "Create all edits that are two edits away from `word`."
	    return (e2 for e1 in self.edits_one(word) for e2 in self.edits_one(e1))
	def known(self,words):
	    "The subset of `words` that appear in the `all_words`."
	    supportedCities = ['ahmedabad', 'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune', 'agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'durg-bhilai nagar', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon', 'guwahati‚ gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur', 'kanpur', 'kakinada', 'kochi', 'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 'pondicherry', 'prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'tiruppur', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 'visakhapatnam', 'warangal']
	    return set(word for word in words if word in supportedCities)

	def our_possible_corrections(self,word):
	    word = word.lower()
	    return (self.known([word]) or self.known(self.edits_one(word)) or self.known(self.edits_two(word)))
	    

	def name(self):
		return 'verify_location'

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("verifying location")
		cityname = tracker.get_slot("location")
		if((cityname is not None) and (cityname.strip())):
			correctedCity = list(self.our_possible_corrections(cityname.strip()))
		else:
			dispatcher.utter_message("slot for location is empty")
			dispatcher.utter_template("utter_ask_location", tracker)
			return [SlotSet("location", None)]

		if len(correctedCity) == 0:
			dispatcher.utter_message("We do not operate in that area yet.")
			dispatcher.utter_template("utter_ask_location", tracker)
			return [SlotSet("location", None)]
		else:
			dispatcher.utter_message("City Found: ")
			dispatcher.utter_message(correctedCity[0])
			return [SlotSet("location", correctedCity[0])]
	
# Action to search the restraurants by calling the Zomato API.
# Here we also sort the restraurants by the rating in the descending order.
# We also populate the slot for html email which will be sent in case the customer wants to have the results in
# email
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('pricerange')
		pricerangeCategory = -1
		if( (budget.find("300") >= 0) & (budget.find("700") >= 0 ) ):
			pricerangeCategory = 1
		elif( (budget.find("300") >= 0) ):
			pricerangeCategory = 0
		elif( (budget.find("700") >= 0) ):
			pricerangeCategory = 2
		else:
			dispatcher.utter_message("Could not understand the price range. Giving restraurants between 300 and 700 Rs")
			pricerangeCategory = 1
		location_detail = zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat = d1["location_suggestions"][0]["latitude"]
		lon = d1["location_suggestions"][0]["longitude"]
		cuisines_dict = {'Chinese':25,'Mexican':73 ,'Italian':55 ,'American':1 ,'Thai':95,'north indian':50,'south indian':85}
        # Fetch the 10 restraurant results by calling the Zomato API
		results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 10)
		d = json.loads(results)
        
        #Map to maintain the restraurant rating and the restraurant result. Will use this map to order by rating
		ratings_map = {}
		ratings_map_html = {}
		response=""
		if d['results_found'] == 0:
			response= "no results"
			dispatcher.utter_message("No restraurants found for your search")
			return [SlotSet('restraurant_results_for_email_message',"No results found")]
		else:
			count = 0
			for restaurant in d['restaurants']:
				if(count == 10):
					break
				cost = restaurant.get('restaurant').get('average_cost_for_two')
				if(pricerangeCategory == 0): # <=300
					if(not cost <= 300):
						continue
				elif(pricerangeCategory == 2): # >=700
					if(not cost >= 700):
						continue
				elif(pricerangeCategory == 1): # 300-700
					if(not ((cost > 300) & (cost < 700))):
						continue
                            # TODO: Maintain a map of restraurant meta, rating, finally sort.
				current_restraurant =  "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " Cost: " + str(cost) + " Rating: " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n"
				current_rating = restaurant['restaurant']['user_rating']['aggregate_rating']
                
				ratings_map[current_restraurant] = current_rating
            
				current_restraurant_html =  "<tr><td>" + restaurant['restaurant']['name']+ "</td><td>"+ restaurant['restaurant']['location']['address']+ "</td><td>" + str(cost) + "</td><td>" + restaurant['restaurant']['user_rating']['aggregate_rating'] + "</td></tr>"
                
				ratings_map_html[current_restraurant_html] = current_rating

				count = count + 1
            
            # Sort the restraurants by rating.
		sorted_restraurants = sorted(ratings_map.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

            # Sort the html email by the rating.
		sorted_restraurants_html = sorted(ratings_map_html.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

		for restraurant in sorted_restraurants:
			response = response + restraurant[0]

        # Utter the response
		dispatcher.utter_message("-----"+response)
            
# Initialize the response_html for the email with the html table header
		response_html = """<table border='1'>
<tr>
<td> <b> Restraurant Name </b> </td>
<td> <b> Restraurant Location </b> </td>
<td> <b> Price - Meal for Two </b> </td>
<td> <b> Rating </b> </td>
</tr>"""
            # Populate the html table content for the email
		for restraurant in sorted_restraurants_html:
			response_html = response_html + restraurant[0]
            
		response_html = response_html + "</table>"
        
		email_subject = 'Your restraurants for ' + cuisine + ' in ' + loc + ' with budget ' + budget

		return [SlotSet('restraurant_results_for_email_message',response_html), SlotSet('location', None),
                SlotSet('cuisine', None), SlotSet('pricerange', None), SlotSet('email_subject', email_subject)]

# Action to send email to the customer. The email subject is dynamic based on the choices selected by the
# customer. Uses gmail smtp server to send the email.
class ActionSendEmail(Action):
    def name(self):
        return 'send_email'
        
    def run(self, dispatcher, tracker, domain):
        email_message = tracker.get_slot("restraurant_results_for_email_message")
        email_id = tracker.get_slot("email")
        # Code to send email
        dispatcher.utter_message("Sending email ...")
        msg = MIMEText(email_message, 'html')

        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('pricerange')

        msg['Subject'] = tracker.get_slot('email_subject')
        msg['From'] = 'Restraurant Bot'
        msg['To'] = email_id
        
        # Handling an error condition when the email id is populated in the slot
        if not email_id:
            dispatcher.utter_message("Did not send email as email id is not entered")
            return

        try:
            smtp_host = 'smtp.gmail.com'
            smtp_port = 587
            server = smtplib.SMTP()
            server.connect(smtp_host,smtp_port)
            server.ehlo()
            server.starttls()
            server.login('kurmakshetra@gmail.com','pho12kus')
            server.sendmail('kurmakshetra@gmail.com', email_id, msg.as_string())
            server.quit()
            print('Email sent!')
        except:
            print('Something went wrong...')
            traceback.print_exc()

        dispatcher.utter_message("Sent. Bon Appetit!")
        return [SlotSet('restraurant_results_for_email_message',None), SlotSet('email_subject', None)]

