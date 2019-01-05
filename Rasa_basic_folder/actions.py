from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
# Import smtplib for the actual sending function
import smtplib
import traceback


class ActionVerifyLocation(Action):
	def name(self):
		return 'verify_location'
	def run(self, dispatcher, tracker, domain):
		cityname = tracker.get_slot("location")
		supportedCities = [
			"Ahmedabad",
			"Bangalore",
			"Chennai",
			"Delhi",
			"Hyderabad",
			"Kolkata",
			"Mumbai",
			"Pune",
			"Agra",
			"Ajmer",
			"Aligarh",
			"Amravati",
			"Amritsar",
			"Asansol",
			"Aurangabad",
			"Bareilly",
			"Belgaum",
			"Bhavnagar",
			"Bhiwandi",
			"Bhopal",
			"Bhubaneswar",
			"Bikaner",
			"Bokaro Steel City",
			"Chandigarh",
			"Coimbatore",
			"Cuttack",
			"Dehradun",
			"Dhanbad",
			"Durg-Bhilai Nagar",
			"Durgapur",
			"Erode",
			"Faridabad",
			"Firozabad",
			"Ghaziabad",
			"Gorakhpur",
			"Gulbarga",
			"Guntur",
			"Gurgaon",
			"Guwahati‚ Gwalior",
			"Hubli-Dharwad",
			"Indore",
			"Jabalpur",
			"Jaipur",
			"Jalandhar",
			"Jammu",
			"Jamnagar",
			"Jamshedpur",
			"Jhansi",
			"Jodhpur",
			"Kannur",
			"Kanpur",
			"Kakinada",
			"Kochi",
			"Kottayam",
			"Kolhapur",
			"Kollam",
			"Kota",
			"Kozhikode",
			"Kurnool",
			"Lucknow",
			"Ludhiana",
			"Madurai",
			"Malappuram",
			"Mathura",
			"Goa",
			"Mangalore",
			"Meerut",
			"Moradabad",
			"Mysore",
			"Nagpur",
			"Nanded",
			"Nashik",
			"Nellore",
			"Noida",
			"Palakkad",
			"Patna",
			"Pondicherry",
			"Prayagraj",
			"Raipur",
			"Rajkot",
			"Rajahmundry",
			"Ranchi",
			"Rourkela",
			"Salem",
			"Sangli",
			"Siliguri",
			"Solapur",
			"Srinagar",
			"Sultanpur",
			"Surat",
			"Thiruvananthapuram",
			"Thrissur",
			"Tiruchirappalli",
			"Tirunelveli",
			"Tiruppur",
			"Ujjain",
			"Bijapur",
			"Vadodara",
			"Varanasi",
			"Vasai-Virar City",
			"Vijayawada",
			"Visakhapatnam",
			"Warangal"
			]
		if cityname.lower() not in [name.lower() for name in supportedCities]:
			dispatcher.utter_message("We do not operate in that area yet.")
			dispatcher.utter_template("utter_ask_location", tracker)
			return [SlotSet("location", None)]
		else:
			dispatcher.utter_message("City Found.")
	

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
			pricerangeCategory = -1
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		#if pricerangeCategory == -1:
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			count = 0
			for restaurant in d['restaurants']:
				if(count == 5):
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
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " Cost: " + str(cost) + "\n"
				count = count + 1
			SlotSet('restraurant_results_for_email_message', response)
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

class ActionSendEmail(Action):
    def name(self):
        return 'send_email'
        
    def run(self, dispatcher, tracker, domain):
        email_message = tracker.get_slot("restraurant_results_for_email_message")
        email_id = tracker.get_slot("email")
# Code to send email
        gmail_user = 'kurmakshetra@gmail.com'
        gmail_password = 'pho12kus'

        sent_from = gmail_user
        to = [email_id]
        subject = 'Your Restraurant Search Results'
        body = email_message

        email_text = """\
            From: %s
            To: %s
            Subject: %s
            
            %s
            """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
            print('Email sent!')
        except:
            print('Something went wrong...')
            traceback.print_exc()

        dispatcher.utter_message("Sent. Bon Appetit!")


			
		


