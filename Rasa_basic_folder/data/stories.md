## Generated Story -7299120857403942656
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - verify_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrishikesh.r.desai@gmail.com"}
    - slot{"email": "hrishikesh.r.desai@gmail.com"}
    - send_email


## Generated Story 7571176434215927340
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_should_send_email
* deny

    - export	
## Generated Story 5793991498973845777
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "bengaluru"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
    - export	

## Generated Story -4119916223930012371
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export


## Generated Story 4371494193400271207
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
    - export

## Generated Story -6574399902414284621
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - verify_location
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
	
## Generated Story 8455316801529394086
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - verify_location
    - utter_ask_cuisine
* restaurant_search
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story 8614594228142126930
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - verify_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
    - export

## Generated Story 1806342198547553734
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "bangalore", "pricerange": "700"}
    - slot{"cuisine": "american"}
    - slot{"location": "bangalore"}
    - slot{"pricerange": "700"}
    - verify_location
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export

## Generated Story 4508088622285753629
* greet
    - utter_greet
* restaurant_search{"location": "belgaum", "pricerange": "300 to 700"}
    - slot{"location": "belgaum"}
    - slot{"pricerange": "300 to 700"}
    - verify_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "belgaum"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export

## Generated Story -3143433703116657356
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - verify_location
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -5669288759055082475
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found Asia Kitchen By Mainland China in 136, Ground Floor, 1st Cross, 5th Block, Jyoti Niwas College Road, Koramangala 5th Block, Bangalore Cost: 1500\nFound High Ultra Lounge in 26/1 , 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore Cost: 2600\nFound Yo! Chow in 90/3 Sri Sapthagiri Complex,Outer ring road marathahalli,Opp to innovative Multiplex, Marathahalli, Bangalore Cost: 800\nFound Yauatcha in 1 MG Mall, MG Road, Bangalore Cost: 2800\nFound Mainland China in 28/2, 1st Floor, Siddapura, Whitefield Main Road, Whitefield, Bangalore near Dmart Cost: 1700\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export

## Generated Story 8414988504950852106
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found Asia Kitchen By Mainland China in 136, Ground Floor, 1st Cross, 5th Block, Jyoti Niwas College Road, Koramangala 5th Block, Bangalore Cost: 1500\nFound High Ultra Lounge in 26/1 , 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore Cost: 2600\nFound Yo! Chow in 90/3 Sri Sapthagiri Complex,Outer ring road marathahalli,Opp to innovative Multiplex, Marathahalli, Bangalore Cost: 800\nFound Yauatcha in 1 MG Mall, MG Road, Bangalore Cost: 2800\nFound Mainland China in 28/2, 1st Floor, Siddapura, Whitefield Main Road, Whitefield, Bangalore near Dmart Cost: 1700\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story 4887725827197572356
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300 to 700"}
    - slot{"pricerange": "300 to 700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found RP's Pizzeria in Shop 5, Ground Floor, Axiom 2, SP Ring Road, Bopal, Ahmedabad Cost: 500\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -4361798139229803469
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found The Esplendido Cafe in Ground Floor & First Floor, Opposite Samartheshwar Mahadev, Near V-Mart, Law Garden Cross Road, Navrangpura, Ahmedabad Cost: 800\nFound Makeba - The Lounge Cafe in 8th Floor, 3rd Eye Vision, Opposite Shivalik Plaza, Panjrapol Circle, IIM Road, Vastrapur, Ahmedabad Cost: 1000\nFound Huber & Holly in 7 B, below pakwan restaurnat, pakwan cross road, Boadakdev, Ahmedabad  Cost: 700\nFound Bogarosa in 299/1, Behind Rajpath Club, Beside 9th Avenue Building, Bodakdev, Ahmedabad Cost: 800\n"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email

## Generated Story 8340272776975179895
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -636448589031215344
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300 to 700"}
    - slot{"pricerange": "300 to 700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found RP's Pizzeria in Shop 5, Ground Floor, Axiom 2, SP Ring Road, Bopal, Ahmedabad Cost: 500\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -2716849534532737595
* greet
    - utter_greet
* restaurant_search{"cuisine": "nice"}
    - slot{"cuisine": "nice"}
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300 and 700"}
    - slot{"pricerange": "300 and 700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found RP's Pizzeria in Shop 5, Ground Floor, Axiom 2, SP Ring Road, Bopal, Ahmedabad Cost: 500\n"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "nice"}
    - slot{"cuisine": "nice"}
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found The Esplendido Cafe in Ground Floor & First Floor, Opposite Samartheshwar Mahadev, Near V-Mart, Law Garden Cross Road, Navrangpura, Ahmedabad Cost: 800\nFound Makeba - The Lounge Cafe in 8th Floor, 3rd Eye Vision, Opposite Shivalik Plaza, Panjrapol Circle, IIM Road, Vastrapur, Ahmedabad Cost: 1000\nFound Huber & Holly in 7 B, Pakwan Cross Road, Boadakdev, Ahmedabad Cost: 800\nFound Bogarosa in 299/1, Behind Rajpath Club, Beside 9th Avenue Building, Bodakdev, Ahmedabad Cost: 800\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
* greet
    - utter_greet
* restaurant_search{"cuisine": "nice"}
    - slot{"cuisine": "nice"}
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300 and 700"}
    - slot{"pricerange": "300 and 700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found RP's Pizzeria in Shop 5, Ground Floor, Axiom 2, SP Ring Road, Bopal, Ahmedabad Cost: 500\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
* greet
    - utter_greet
* restaurant_search{"cuisine": "nice"}
    - slot{"cuisine": "nice"}
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found The Esplendido Cafe in Ground Floor & First Floor, Opposite Samartheshwar Mahadev, Near V-Mart, Law Garden Cross Road, Navrangpura, Ahmedabad Cost: 800\nFound Makeba - The Lounge Cafe in 8th Floor, 3rd Eye Vision, Opposite Shivalik Plaza, Panjrapol Circle, IIM Road, Vastrapur, Ahmedabad Cost: 1000\nFound Huber & Holly in 7 B, Pakwan Cross Road, Boadakdev, Ahmedabad Cost: 800\nFound Bogarosa in 299/1, Behind Rajpath Club, Beside 9th Avenue Building, Bodakdev, Ahmedabad Cost: 800\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
## Generated Story -2716849534532737595
* greet
    - utter_greet
* restaurant_search{"cuisine": "nice"}
    - slot{"cuisine": "nice"}
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300 and 700"}
    - slot{"pricerange": "300 and 700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found RP's Pizzeria in Shop 5, Ground Floor, Axiom 2, SP Ring Road, Bopal, Ahmedabad Cost: 500\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
* greet
    - utter_greet
* restaurant_search{"cuisine": "nice"}
    - slot{"cuisine": "nice"}
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found The Esplendido Cafe in Ground Floor & First Floor, Opposite Samartheshwar Mahadev, Near V-Mart, Law Garden Cross Road, Navrangpura, Ahmedabad Cost: 800\nFound Makeba - The Lounge Cafe in 8th Floor, 3rd Eye Vision, Opposite Shivalik Plaza, Panjrapol Circle, IIM Road, Vastrapur, Ahmedabad Cost: 1000\nFound Huber & Holly in 7 B, Pakwan Cross Road, Boadakdev, Ahmedabad Cost: 800\nFound Bogarosa in 299/1, Behind Rajpath Club, Beside 9th Avenue Building, Bodakdev, Ahmedabad Cost: 800\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
* greet
    - utter_greet
* restaurant_search{"cuisine": "nice"}
    - slot{"cuisine": "nice"}
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300 and 700"}
    - slot{"pricerange": "300 and 700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found RP's Pizzeria in Shop 5, Ground Floor, Axiom 2, SP Ring Road, Bopal, Ahmedabad Cost: 500\n"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "nice"}
    - slot{"cuisine": "nice"}
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found The Esplendido Cafe in Ground Floor & First Floor, Opposite Samartheshwar Mahadev, Near V-Mart, Law Garden Cross Road, Navrangpura, Ahmedabad Cost: 800\nFound Makeba - The Lounge Cafe in 8th Floor, 3rd Eye Vision, Opposite Shivalik Plaza, Panjrapol Circle, IIM Road, Vastrapur, Ahmedabad Cost: 1000\nFound Huber & Holly in 7 B, Pakwan Cross Road, Boadakdev, Ahmedabad Cost: 800\nFound Bogarosa in 299/1, Behind Rajpath Club, Beside 9th Avenue Building, Bodakdev, Ahmedabad Cost: 800\n"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search
    - export

## Generated Story 8742619952400058011
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300 and 700"}
    - slot{"pricerange": "300 and 700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found Kovallam in Opposite Sardar Patel Sewa Samaj Hall, C G Road, Ahmedabad Cost: 500\nFound Dakshinayan in 4-7, Sarthik Complex, Near Gulmohar Park Mall, Satellite, Ahmedabad Cost: 600\nFound Radhika's Authentic South Indian Food in 4, 15 - Sunrise Shopping Centre, Near ASIA School, Drive In Road, Gurukul, Ahmedabad Cost: 600\nFound Sankalp in Samir Building, Opposite Municipal Market, C G Road, Ahmedabad Cost: 650\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found Dravida - The Fern in The Fern, Near Sola Overbridge, SG Highway, Sola, Ahmedabad Cost: 1500\n"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "nice"}
    - slot{"cuisine": "nice"}
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300 and 700"}
    - slot{"pricerange": "300 and 700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found Jassi De Parathe in 107, Safal Pegasus, Anand Nagar Road, Prahlad Nagar, Ahmedabad Cost: 650\nFound Food On Way in Satellite Cost: 400\n"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found Jassi De Parathe in 28, Sardar Centre, Vastrapur, Ahmedabad Cost: 700\nFound Barbeque Nation in 1st Floor, Satyaone, Opposite Manav Mandir, Memnagar, Ahmedabad Cost: 1500\nFound The Secret Kitchen in 2nd Floor, Times Square II,\nBeside Avalon Hotel, Sindhu Bhavan Road, Bodakdev, Ahmedabad Cost: 1100\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -6992475329185366927
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "ahmedabad"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "ahmedabad"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found The Esplendido Cafe in Ground Floor & First Floor, Opposite Samartheshwar Mahadev, Near V-Mart, Law Garden Cross Road, Navrangpura, Ahmedabad Cost: 800\nFound Makeba - The Lounge Cafe in 8th Floor, 3rd Eye Vision, Opposite Shivalik Plaza, Panjrapol Circle, IIM Road, Vastrapur, Ahmedabad Cost: 1000\nFound Huber & Holly in 7 B, Pakwan Cross Road, Boadakdev, Ahmedabad Cost: 800\nFound Bogarosa in 299/1, Behind Rajpath Club, Beside 9th Avenue Building, Bodakdev, Ahmedabad Cost: 800\n"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
    - export
## Generated Story 6342505704568343235
* greet
    - utter_greet
* restaurant_search{"location": "ahmedabad", "pricerange": "700"}
    - slot{"location": "ahmedabad"}
    - slot{"pricerange": "700"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found The Esplendido Cafe in Ground Floor & First Floor, Opposite Samartheshwar Mahadev, Near V-Mart, Law Garden Cross Road, Navrangpura, Ahmedabad Cost: 800\nFound Makeba - The Lounge Cafe in 8th Floor, 3rd Eye Vision, Opposite Shivalik Plaza, Panjrapol Circle, IIM Road, Vastrapur, Ahmedabad Cost: 1000\nFound Huber & Holly in 7 B, Pakwan Cross Road, Boadakdev, Ahmedabad Cost: 800\nFound Bogarosa in 299/1, Behind Rajpath Club, Beside 9th Avenue Building, Bodakdev, Ahmedabad Cost: 800\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -1289030032490395016
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "ahmedabad", "pricerange": "700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "ahmedabad"}
    - slot{"pricerange": "700"}
    - verify_location
    - slot{"location": "ahmedabad"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found The Esplendido Cafe in Ground Floor & First Floor, Opposite Samartheshwar Mahadev, Near V-Mart, Law Garden Cross Road, Navrangpura, Ahmedabad Cost: 800\nFound Makeba - The Lounge Cafe in 8th Floor, 3rd Eye Vision, Opposite Shivalik Plaza, Panjrapol Circle, IIM Road, Vastrapur, Ahmedabad Cost: 1000\nFound Huber & Holly in 7 B, Pakwan Cross Road, Boadakdev, Ahmedabad Cost: 800\nFound Bogarosa in 299/1, Behind Rajpath Club, Beside 9th Avenue Building, Bodakdev, Ahmedabad Cost: 800\n"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
    - export
## Generated Story 3157057833187783964
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bangalore", "pricerange": "700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"pricerange": "700"}
    - verify_location
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore Cost: 1600\nFound Byg Brewski Brewing Company in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore Cost: 1600\nFound Brew and Barbeque - A Microbrewery Pub in 36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore Cost: 1400\nFound The Black Pearl in 20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore Cost: 1500\nFound The Reservoire in 17th Main Road, JNC Road, Koramangala 5th Block, Bangalore Cost: 1300\nFound Bombay Adda in 6, Z1 Construction Building, 5th Floor, Next To Sapna Book House, 20th Main Road, Koramangala 7th Block, Bangalore Cost: 1100\nFound Big Pitcher in LR Arcade,4121, Old Airport Road, Bangalore Cost: 1800\nFound Stories in Shop 77, West of Chord Road, Beside To Mahalakshmi Layout Metro Station, Rajajinagar, Bangalore Cost: 1000\nFound XOOX Brewmill in 8, Koramanagala Industrial Layout, Near HDFC Bank, Koramangala 5th Block, Bangalore Cost: 1500\nFound Truffles in 28, 4th 'B' Cross, Koramangala 5th Block, Bangalore Cost: 900\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bangalore", "pricerange": "700", "email": "hrudaya21@gmail.com"}
    - slot{"cuisine": "chinese"}
    - slot{"email": "hrudaya21@gmail.com"}
    - slot{"location": "bangalore"}
    - slot{"pricerange": "700"}
    - verify_location
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore Cost: 1600\nFound Byg Brewski Brewing Company in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore Cost: 1600\nFound Brew and Barbeque - A Microbrewery Pub in 36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore Cost: 1400\nFound The Black Pearl in 20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore Cost: 1500\nFound The Reservoire in 17th Main Road, JNC Road, Koramangala 5th Block, Bangalore Cost: 1300\nFound Bombay Adda in 6, Z1 Construction Building, 5th Floor, Next To Sapna Book House, 20th Main Road, Koramangala 7th Block, Bangalore Cost: 1100\nFound Big Pitcher in LR Arcade,4121, Old Airport Road, Bangalore Cost: 1800\nFound Stories in Shop 77, West of Chord Road, Beside To Mahalakshmi Layout Metro Station, Rajajinagar, Bangalore Cost: 1000\nFound XOOX Brewmill in 8, Koramanagala Industrial Layout, Near HDFC Bank, Koramangala 5th Block, Bangalore Cost: 1500\nFound Truffles in 28, 4th 'B' Cross, Koramangala 5th Block, Bangalore Cost: 900\n"}
	- utter_ask_should_send_email
* affirm
	- utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
    - export
## Generated Story 6690436840854442928
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "banagalore", "pricerange": "700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "banagalore"}
    - slot{"pricerange": "700"}
    - verify_location
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore Cost: 1600\nFound Byg Brewski Brewing Company in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore Cost: 1600\nFound Brew and Barbeque - A Microbrewery Pub in 36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore Cost: 1400\nFound The Black Pearl in 20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore Cost: 1500\nFound The Reservoire in 17th Main Road, JNC Road, Koramangala 5th Block, Bangalore Cost: 1300\nFound Bombay Adda in 6, Z1 Construction Building, 5th Floor, Next To Sapna Book House, 20th Main Road, Koramangala 7th Block, Bangalore Cost: 1100\nFound Big Pitcher in LR Arcade,4121, Old Airport Road, Bangalore Cost: 1800\nFound Stories in Shop 77, West of Chord Road, Beside To Mahalakshmi Layout Metro Station, Rajajinagar, Bangalore Cost: 1000\nFound XOOX Brewmill in 8, Koramanagala Industrial Layout, Near HDFC Bank, Koramangala 5th Block, Bangalore Cost: 1500\nFound Truffles in 28, 4th 'B' Cross, Koramangala 5th Block, Bangalore Cost: 900\n"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story 3325202526855132928
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found CTR in 7th Cross, Margosa Road, Malleshwaram, Bangalore Cost: 150\nFound Taaza Thindi in 1004, 26th Main, Next to HDFC Bank, 4th T Block, Jayanagar, Bangalore Cost: 100\nFound Vidyarthi Bhavan in 32, Gandhi Bazaar, Near Gandhi Bazaar Circle, Basavanagudi, Bangalore Cost: 150\nFound Mavalli Tiffin Room (MTR) in 14, Lalbagh Road, Mavalli, Basavanagudi, Bangalore Cost: 250\nFound Veena Stores in 187, 15th Cross, Margosa Road, Malleshwaram, Bangalore Cost: 150\nFound Mavalli Tiffin Room (MTR) in Namma Metro Pillar 62, 100 Feet Road, Indiranagar, Bangalore Cost: 300\nFound Brahmin's Coffee Bar in Ranga Rao Road, Near Shankar Mutt, Shankarapura, Near Basavanagudi, Bangalore Cost: 100\nFound Sree Krishna Kafe in 5th Main, Near Muni Reddy Kalyana Mantap, Koramangala 5th Block, Bangalore Cost: 200\n"}
    - utter_ask_should_send_email
* deny
* goodbye
    - utter_goodbye
    - export
## Generated Story 8467491363686640672
* greet
    - utter_greet
* goodbye
    - utter_goodbye
* greet
    - utter_greet
* goodbye
    - utter_goodbye
* greet
    - utter_greet
* goodbye
    - utter_goodbye
* greet
    - utter_greet
* goodbye
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* goodbye
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "pricerange": "700"}
    - slot{"location": "bangalore"}
    - slot{"pricerange": "700"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "Found Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore Cost: 1600\nFound Byg Brewski Brewing Company in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore Cost: 1600\nFound Brew and Barbeque - A Microbrewery Pub in 36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore Cost: 1400\nFound The Black Pearl in 20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore Cost: 1500\nFound The Reservoire in 17th Main Road, JNC Road, Koramangala 5th Block, Bangalore Cost: 1300\nFound Bombay Adda in 6, Z1 Construction Building, 5th Floor, Next To Sapna Book House, 20th Main Road, Koramangala 7th Block, Bangalore Cost: 1100\nFound Big Pitcher in LR Arcade,4121, Old Airport Road, Bangalore Cost: 1800\nFound Stories in Shop 77, West of Chord Road, Beside To Mahalakshmi Layout Metro Station, Rajajinagar, Bangalore Cost: 1000\nFound XOOX Brewmill in 8, Koramanagala Industrial Layout, Near HDFC Bank, Koramangala 5th Block, Bangalore Cost: 1500\nFound Truffles in 28, 4th 'B' Cross, Koramangala 5th Block, Bangalore Cost: 900\n"}
    - utter_ask_should_send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -4455684189492410837
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "london"}
    - slot{"location": "london"}
    - verify_location
    - slot{"location": null}
* restaurant_search{"location": "baklsdkan"}
    - slot{"location": "baklsdkan"}
    - verify_location
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>Byg Brewski Brewing Company</td><td>Behind MK Retail, Sarjapur Road, Bangalore</td><td>1600</td><td>4.9</td></tr><tr><td>The Black Pearl</td><td>20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore</td><td>1500</td><td>4.7</td></tr><tr><td>Brew and Barbeque - A Microbrewery Pub</td><td>36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore</td><td>1400</td><td>4.7</td></tr><tr><td>Big Pitcher</td><td>LR Arcade,4121, Old Airport Road, Bangalore</td><td>1800</td><td>4.7</td></tr><tr><td>Byg Brewski Brewing Company</td><td>22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore</td><td>1600</td><td>4.6</td></tr><tr><td>XOOX Brewmill</td><td>8, Koramanagala Industrial Layout, Near HDFC Bank, Koramangala 5th Block, Bangalore</td><td>1500</td><td>4.5</td></tr><tr><td>The Reservoire</td><td>17th Main Road, JNC Road, Koramangala 5th Block, Bangalore</td><td>1300</td><td>4.5</td></tr><tr><td>Stories</td><td>Shop 77, West of Chord Road, Beside To Mahalakshmi Layout Metro Station, Rajajinagar, Bangalore</td><td>1000</td><td>4.3</td></tr><tr><td>Bombay Adda</td><td>6, Z1 Construction Building, 5th Floor, Next To Sapna Book House, 20th Main Road, Koramangala 7th Block, Bangalore</td><td>1100</td><td>4.3</td></tr></table>"}
    - utter_ask_should_send_email
* deny
* goodbye
    - utter_goodbye
    - export

## Generated Story 7020414661036337744
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "london"}
    - slot{"location": "london"}
    - verify_location
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>Byg Brewski Brewing Company</td><td>Behind MK Retail, Sarjapur Road, Bangalore</td><td>1600</td><td>4.9</td></tr><tr><td>The Black Pearl</td><td>20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore</td><td>1500</td><td>4.7</td></tr><tr><td>Brew and Barbeque - A Microbrewery Pub</td><td>36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore</td><td>1400</td><td>4.7</td></tr><tr><td>Big Pitcher</td><td>LR Arcade,4121, Old Airport Road, Bangalore</td><td>1800</td><td>4.7</td></tr><tr><td>Byg Brewski Brewing Company</td><td>22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore</td><td>1600</td><td>4.6</td></tr><tr><td>XOOX Brewmill</td><td>8, Koramanagala Industrial Layout, Near HDFC Bank, Koramangala 5th Block, Bangalore</td><td>1500</td><td>4.5</td></tr><tr><td>The Reservoire</td><td>17th Main Road, JNC Road, Koramangala 5th Block, Bangalore</td><td>1300</td><td>4.5</td></tr><tr><td>Stories</td><td>Shop 77, West of Chord Road, Beside To Mahalakshmi Layout Metro Station, Rajajinagar, Bangalore</td><td>1000</td><td>4.3</td></tr><tr><td>Bombay Adda</td><td>6, Z1 Construction Building, 5th Floor, Next To Sapna Book House, 20th Main Road, Koramangala 7th Block, Bangalore</td><td>1100</td><td>4.3</td></tr></table>"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "amirisetty.vijayaraghavan@gmail.com"}
    - slot{"email": "amirisetty.vijayaraghavan@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -5687885756526430684
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -5687885756526430684
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
    - export
## Generated Story -5687885756526430684
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -5687885756526430684
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
    - export
## Generated Story -5687885756526430684
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": ""}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export	
## Generated Story -7858389892448489130
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300-700"}
    - slot{"pricerange": "300-700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>Shanmukha</td><td>1313, Near Bangalore Central Mall, 25th Main, 9th Block, Jayanagar, Bangalore</td><td>600</td><td>4.3</td></tr></table>"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
## Generated Story -6720322336988311042
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - verify_location
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>Byg Brewski Brewing Company</td><td>Behind MK Retail, Sarjapur Road, Bangalore</td><td>1600</td><td>4.9</td></tr><tr><td>The Black Pearl</td><td>20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore</td><td>1500</td><td>4.7</td></tr><tr><td>Byg Brewski Brewing Company</td><td>22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore</td><td>1600</td><td>4.7</td></tr><tr><td>Brew and Barbeque - A Microbrewery Pub</td><td>36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore</td><td>1400</td><td>4.7</td></tr><tr><td>Big Pitcher</td><td>LR Arcade,4121, Old Airport Road, Bangalore</td><td>1800</td><td>4.7</td></tr><tr><td>The Reservoire</td><td>17th Main Road, JNC Road, Koramangala 5th Block, Bangalore</td><td>1300</td><td>4.5</td></tr><tr><td>XOOX Brewmill</td><td>8, Koramanagala Industrial Layout, Near HDFC Bank, Koramangala 5th Block, Bangalore</td><td>1500</td><td>4.4</td></tr><tr><td>Stories</td><td>Shop 77, West of Chord Road, Beside To Mahalakshmi Layout Metro Station, Rajajinagar, Bangalore</td><td>1000</td><td>4.3</td></tr><tr><td>Bombay Adda</td><td>6, Z1 Construction Building, 5th Floor, Next To Sapna Book House, 20th Main Road, Koramangala 7th Block, Bangalore</td><td>1100</td><td>4.3</td></tr></table>"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye	

## Generated Story -5006001434080967388
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - verify_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr></table>"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -8059867068095969981
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - verify_location
    - slot{"location": null}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - verify_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr></table>"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
	
## Generated Story -8895424187800639138
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - verify_location
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>Bhena Da Dhaba</td><td>SCF 1, Phase 5, Mohali\nNear P.T.L. LIGHT POINT \n(PUNJAB TRACTOR LTD.)</td><td>250</td><td>3.8</td></tr></table>"}
    - utter_ask_should_send_email
* affirm
    - export
	
## Generated Story -2941606674492578074
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300-700"}
    - slot{"pricerange": "300-700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>Shanmukha</td><td>1313, Near Bangalore Central Mall, 25th Main, 9th Block, Jayanagar, Bangalore</td><td>600</td><td>4.3</td></tr></table>"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -3454328211532327734
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - verify_location
    - slot{"location": null}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -1768727931407917541
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"pricerange": "300-700"}
    - slot{"pricerange": "300-700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>Shanmukha</td><td>1313, Near Bangalore Central Mall, 25th Main, 9th Block, Jayanagar, Bangalore</td><td>600</td><td>4.3</td></tr></table>"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -628339774967404618
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - verify_location
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>Byg Brewski Brewing Company</td><td>Behind MK Retail, Sarjapur Road, Bangalore</td><td>1600</td><td>4.9</td></tr><tr><td>The Black Pearl</td><td>20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore</td><td>1500</td><td>4.7</td></tr><tr><td>Byg Brewski Brewing Company</td><td>22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore</td><td>1600</td><td>4.7</td></tr><tr><td>Brew and Barbeque - A Microbrewery Pub</td><td>36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore</td><td>1400</td><td>4.7</td></tr><tr><td>Big Pitcher</td><td>LR Arcade,4121, Old Airport Road, Bangalore</td><td>1800</td><td>4.7</td></tr><tr><td>The Reservoire</td><td>17th Main Road, JNC Road, Koramangala 5th Block, Bangalore</td><td>1300</td><td>4.5</td></tr><tr><td>XOOX Brewmill</td><td>8, Koramanagala Industrial Layout, Near HDFC Bank, Koramangala 5th Block, Bangalore</td><td>1500</td><td>4.4</td></tr><tr><td>Stories</td><td>Shop 77, West of Chord Road, Beside To Mahalakshmi Layout Metro Station, Rajajinagar, Bangalore</td><td>1000</td><td>4.3</td></tr><tr><td>Bombay Adda</td><td>6, Z1 Construction Building, 5th Floor, Next To Sapna Book House, 20th Main Road, Koramangala 7th Block, Bangalore</td><td>1100</td><td>4.3</td></tr></table>"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* goodbye
    - utter_goodbye
    - export
## Generated Story -1029740409939403728
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - verify_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>The Saffron Tree</td><td>100, Raja Basanta Roy Road, Southern Avenue</td><td>1000</td><td>4.8</td></tr><tr><td>Spice Kraft</td><td>54/1/2A, Hazra Road, Ballygunge Phari, Near Hazra Law College, Ballygunge, Kolkata</td><td>1200</td><td>4.8</td></tr><tr><td>Barbeque Nation</td><td>1st Floor, 24, Park Center Building, Park Street Area, Kolkata</td><td>1800</td><td>4.8</td></tr><tr><td>JW Kitchen - JW Marriott Hotel Kolkata</td><td>JW Marriott Hotel Kolkata, 4A, J.B.S Haldane Avenue, Science City Area, Kolkata</td><td>3000</td><td>4.6</td></tr><tr><td>Five Mad Men</td><td>Omega Building Of Bengal Intelligence Park, 1st Floor Plot A2, M2 &N2, Block EP &GP, Salt Lake Electronic Complex, Sector 5, Salt Lake, Kolkata</td><td>1000</td><td>4.6</td></tr><tr><td>Chez - Pan Oriental Kitchen</td><td>D/26, Bapuji Nagar, Near Ekta Heights Building,  Baghajatin, Kolkata</td><td>800</td><td>4.6</td></tr><tr><td>What's Up</td><td>122A, Southern Avenue, Kolkata</td><td>1000</td><td>4.5</td></tr><tr><td>The Awadh Restaurant</td><td>17, Park Circus Area, Kolkata</td><td>1200</td><td>4.5</td></tr><tr><td>Carpe Diem</td><td>18M Park Street Area, Kolkata</td><td>1000</td><td>4.5</td></tr><tr><td>Tram Deepo</td><td>45, 2nd Floor, Syed Amir Ali Avenue, Near Quest Mall, Ballygunge, Kolkata</td><td>1200</td><td>3.9</td></tr></table>"}
    - utter_ask_should_send_email
* deny
* goodbye
    - utter_goodbye
    - export
## Generated Story 5883706087508893027
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - verify_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>Mitron - Peninsula Grand Hotel</td><td>Hotel Peninsula Grand, Rooftop, Opposite Sakinaka Metro Station, Andheri Airport Road, Sakinaka, Mumbai</td><td>800</td><td>4.9</td></tr><tr><td>JLWA</td><td>3rd Floor, VN Sphere Turner, Linking Road, Bandra West</td><td>1600</td><td>4.9</td></tr><tr><td>Tamasha</td><td>Ground Floor, Victoria House, E.B Marg, Lower Parel, Mumbai</td><td>1800</td><td>4.8</td></tr><tr><td>Plum by Bent Chair</td><td>Third Floor, Trade View Building, Kamala Mills Compound, Senapati Bapat Marg, Lower Parel, Mumbai</td><td>1800</td><td>4.8</td></tr><tr><td>R' ADDA</td><td>Ramee Guestline Hotel, 462, A B Nair Road, Juhu, Mumbai</td><td>1200</td><td>4.7</td></tr><tr><td>Lord of the Drinks</td><td>Third Floor, Trade View Building, Kamala Mills Compound, Senapati Bapat Marg, Lower Parel, Mumbai</td><td>1500</td><td>4.7</td></tr><tr><td>HITCHKI</td><td>5, Transocean, Hiranandani Business Park, Lake Boulevard Road, Powai, Mumbai</td><td>1200</td><td>4.7</td></tr><tr><td>Carter Road Social</td><td>21, Gagangiri CHS Ltd, Carter Road, Bandra West, Mumbai</td><td>1400</td><td>4.6</td></tr><tr><td>House Of Tipsy</td><td>3/4, Dheeraj Pali Arcade, Dr. Ambedkar Road, Pali Naka, Pali Hill, Bandra West</td><td>1800</td><td>4.5</td></tr><tr><td>BKC  DIVE</td><td>Ground Floor, Pinnacle Corporate Park, Next To Trade Centre, Opposite MTNL Office, Bandra Kurla Complex, Mumbai</td><td>1000</td><td>4.5</td></tr></table>"}
    - utter_ask_should_send_email
* deny
* goodbye
    - utter_goodbye
    - export
## Generated Story -3444613021654089763
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - verify_location
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>The Hedgehog Caf\u00e9</td><td>SCF 12, Inner Market, Sector 7 C, Near, Sector 7, Chandigarh</td><td>1200</td><td>4.8</td></tr><tr><td>Sector 7 Social</td><td>SCO 37, Madhya Marg, Sector 7, Chandigarh</td><td>1400</td><td>4.7</td></tr><tr><td>Falcon Cafe Lounge</td><td>Site 5, Sector 16, Panchkula</td><td>1100</td><td>4.7</td></tr><tr><td>CAF\u00c8 JC's</td><td>Shop 2 & 3, Coal Depot Complex, Sector 10 D, Sector 10, Chandigarh</td><td>1200</td><td>4.6</td></tr><tr><td>Boathouse</td><td>Ground Floor, Adjacent to Volvo Showroom, Elante Mall, Chandigarh Industrial Area, Chandigarh</td><td>1500</td><td>4.5</td></tr><tr><td>Food@U</td><td>Plot 102, Industrial Area Phase 2, Chandigarh Industrial Area, Chandigarh</td><td>700</td><td>4.2</td></tr><tr><td>Amrit Sweets</td><td>SCF 78, Phase 5, Mohali</td><td>700</td><td>4.0</td></tr></table>"}
    - utter_ask_should_send_email
* deny
* goodbye
    - utter_goodbye
    - export
## Generated Story 7771344804806408635
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>Byg Brewski Brewing Company</td><td>Behind MK Retail, Sarjapur Road, Bangalore</td><td>1600</td><td>4.9</td></tr><tr><td>The Black Pearl</td><td>20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore</td><td>1500</td><td>4.7</td></tr><tr><td>Byg Brewski Brewing Company</td><td>22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore</td><td>1600</td><td>4.7</td></tr><tr><td>Brew and Barbeque - A Microbrewery Pub</td><td>36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore</td><td>1400</td><td>4.7</td></tr><tr><td>Big Pitcher</td><td>LR Arcade,4121, Old Airport Road, Bangalore</td><td>1800</td><td>4.7</td></tr><tr><td>The Reservoire</td><td>17th Main Road, JNC Road, Koramangala 5th Block, Bangalore</td><td>1300</td><td>4.5</td></tr><tr><td>XOOX Brewmill</td><td>8, Koramanagala Industrial Layout, Near HDFC Bank, Koramangala 5th Block, Bangalore</td><td>1500</td><td>4.4</td></tr><tr><td>Stories</td><td>Shop 77, West of Chord Road, Beside To Mahalakshmi Layout Metro Station, Rajajinagar, Bangalore</td><td>1000</td><td>4.3</td></tr><tr><td>Bombay Adda</td><td>6, Z1 Construction Building, 5th Floor, Next To Sapna Book House, 20th Main Road, Koramangala 7th Block, Bangalore</td><td>1100</td><td>4.3</td></tr></table>"}
    - utter_ask_should_send_email
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
## Generated Story 7293205124992999431
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>Byg Brewski Brewing Company</td><td>Behind MK Retail, Sarjapur Road, Bangalore</td><td>1600</td><td>4.9</td></tr><tr><td>The Black Pearl</td><td>20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore</td><td>1500</td><td>4.7</td></tr><tr><td>Byg Brewski Brewing Company</td><td>22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore</td><td>1600</td><td>4.7</td></tr><tr><td>Brew and Barbeque - A Microbrewery Pub</td><td>36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore</td><td>1400</td><td>4.7</td></tr><tr><td>Big Pitcher</td><td>LR Arcade,4121, Old Airport Road, Bangalore</td><td>1800</td><td>4.7</td></tr><tr><td>The Reservoire</td><td>17th Main Road, JNC Road, Koramangala 5th Block, Bangalore</td><td>1300</td><td>4.5</td></tr><tr><td>XOOX Brewmill</td><td>8, Koramanagala Industrial Layout, Near HDFC Bank, Koramangala 5th Block, Bangalore</td><td>1500</td><td>4.4</td></tr><tr><td>Stories</td><td>Shop 77, West of Chord Road, Beside To Mahalakshmi Layout Metro Station, Rajajinagar, Bangalore</td><td>1000</td><td>4.3</td></tr><tr><td>Bombay Adda</td><td>6, Z1 Construction Building, 5th Floor, Next To Sapna Book House, 20th Main Road, Koramangala 7th Block, Bangalore</td><td>1100</td><td>4.3</td></tr></table>"}
    - utter_ask_should_send_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bangalore", "pricerange": "700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"pricerange": "700"}
    - verify_location
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"restraurant_results_for_email_message": "<table border='1'>\n<tr>\n<td> <b> Restraurant Name </b> </td>\n<td> <b> Restraurant Location </b> </td>\n<td> <b> Price - Meal for Two </b> </td>\n<td> <b> Rating </b> </td>\n</tr><tr><td>Byg Brewski Brewing Company</td><td>Behind MK Retail, Sarjapur Road, Bangalore</td><td>1600</td><td>4.9</td></tr><tr><td>The Black Pearl</td><td>20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore</td><td>1500</td><td>4.7</td></tr><tr><td>Byg Brewski Brewing Company</td><td>22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore</td><td>1600</td><td>4.7</td></tr><tr><td>Brew and Barbeque - A Microbrewery Pub</td><td>36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore</td><td>1400</td><td>4.7</td></tr><tr><td>Big Pitcher</td><td>LR Arcade,4121, Old Airport Road, Bangalore</td><td>1800</td><td>4.7</td></tr><tr><td>The Reservoire</td><td>17th Main Road, JNC Road, Koramangala 5th Block, Bangalore</td><td>1300</td><td>4.5</td></tr><tr><td>XOOX Brewmill</td><td>8, Koramanagala Industrial Layout, Near HDFC Bank, Koramangala 5th Block, Bangalore</td><td>1500</td><td>4.4</td></tr><tr><td>Stories</td><td>Shop 77, West of Chord Road, Beside To Mahalakshmi Layout Metro Station, Rajajinagar, Bangalore</td><td>1000</td><td>4.3</td></tr><tr><td>Bombay Adda</td><td>6, Z1 Construction Building, 5th Floor, Next To Sapna Book House, 20th Main Road, Koramangala 7th Block, Bangalore</td><td>1100</td><td>4.3</td></tr></table>"}
    - utter_ask_should_send_email
* deny
    - utter_goodbye