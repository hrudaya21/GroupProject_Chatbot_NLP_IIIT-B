from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-522725529030-522376611319-521772758960-b47293f491e900722feb7cfba9123f69', #app verification token
							'xoxb-522725529030-523246230679-I1oLwNBN45wSPJE8zdQDkyH2', # bot verification token
							'wKOVPESU40CnTxBxGpffs9ko', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))