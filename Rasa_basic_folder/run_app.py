from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-514713642004-514881404818-520787223217-0a6c307f750bb595d0f0a5dcdb60cc11', #app verification token
							'xoxb-514713642004-514782809987-2C6Ezn4FJN3HKsEd6fm2KL71', # bot verification token
							'fUOT7btJnfJcWInqqP8OgwYC', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))