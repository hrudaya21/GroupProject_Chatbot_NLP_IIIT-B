## Generated Story 255706069223404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## Generated Story 1993277579540566202
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_restaurant
    - utter_goodbye

## Generated Story 3320800183399695936
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
* goodbye
    - utter_goodbye

## Generated Story -4639179087166749998
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "delhi"}
    - export


## Generated Story 4963448062290237512
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
* affirm
    - utter_goodbye
    - export

## Generated Story -2639717325624473810
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
* restaurant_search{"pricerange": "300 to 700"}
    - slot{"pricerange": "300 to 700"}
    - export
## Generated Story 6355795001964485975
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
    - export
## Generated Story 5216608032655389217
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - export	
## Generated Story 4608350022065743812
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
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - export	
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
* send_email
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
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
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
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
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
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "hrudaya21@gmail.com"}
    - slot{"email": "hrudaya21@gmail.com"}
    - send_email
    - export