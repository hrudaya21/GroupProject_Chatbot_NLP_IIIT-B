from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-522725529030-522376611319-522088662883-6adf2dc7d48479182ae058685c04bf31', #app verification token
							'xoxb-522725529030-523246230679-vBz86hxUyoifTwKdwQ0c1vXD', # bot verification token
							'wKOVPESU40CnTxBxGpffs9ko', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))