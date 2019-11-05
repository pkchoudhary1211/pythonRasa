# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

# @socketio.on('user_uttered')
#     def handle_message(message):
#         print("user")
        # do something
# from rasa_core.channels.socketio import SocketIOInput
# from rasa_core.agent import Agent
# from rasa_core.interpreter import NaturalLanguageInterpreter

# # load your trained agent
# interpreter = NaturalLanguageInterpreter.create('./models/nlu-20191104-123048.tar.gz')
# agent = Agent.load('./models/core-20191104-143951.tar.gz', interpreter=interpreter)
# input_channel = SocketIOInput(
#             # event name for messages sent from the user
#             user_message_evt="user_uttered",
#             # event name for messages sent from the bot
#             bot_message_evt="bot_uttered",
#             # socket.io namespace to use for the messages
#             namespace=None
#         )
# # set serve_forever=False if you want to keep the server running
# s = agent.handle_channels([input_channel], 5005, serve_forever=True)