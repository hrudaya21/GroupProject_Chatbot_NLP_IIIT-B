from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-514713642004-514881404818-515940346263-24b03666d3a7cbd1e60558089993b7ef', #app verification token
							'xoxb-514713642004-514782809987-t8OYq1Bdfy3rdFSVGeXnok86', # bot verification token
							'fUOT7btJnfJcWInqqP8OgwYC', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))