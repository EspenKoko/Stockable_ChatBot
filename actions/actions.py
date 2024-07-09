# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
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
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from rasa_sdk.events import SlotSet , SessionStarted, ActionExecuted, EventType, UserUttered

import webbrowser

class GreetAction(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = next(tracker.get_latest_input_channel())

        # Access the recognized synonym values for an entity
        synonym_values = tracker.get_slot("entity_name")

        # Access a specific synonym value
        first_synonym = synonym_values[0]

        # Use the synonym values in your response or custom logic
        dispatcher.utter_message(f"Hello! You mentioned {first_synonym}. How can I assist you?")
        return []




from rasa_sdk.types import DomainDict



class ActionNavigateToURL(Action):
    def name(self) -> Text:
        return "action_navigate_to_url"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        # Get the user's intent
        intent = tracker.latest_message['intent'].get('name')
        
        # Define URLs based on intents
        url_mapping = {
            "dashboard_affirm": "http://localhost:4200/client-dashboard",
            "log_error_affirm": "http://localhost:4200/log-error",
            "store_affirm": "http://localhost:4200/acs-store",
            "printers_affirm": "http://localhost:4200/client-printers",
            "make_payment_affirm": "http://localhost:4200/make-payment",
            "payment_history_affirm": "http://localhost:4200/payment-history",
            "help_affirm": "http://localhost:4200/FAQs",
            "account_affirm": "http://localhost:4200/account",
            "change_password_affirm": "http://localhost:4200/change-password",
            "contact_us_affirm": "https://www.acs-group.com/about/contact-us",
            "location_info_affirm": "https://www.google.com/maps/place/Takealot+Central+Office/@-33.9184311,18.4284028,15z/data=!4m6!3m5!1s0x1dcc5d88dddb4bfd:0xf34157712fde5e18!8m2!3d-33.9184311!4d18.4284028!16s%2Fg%2F11b5ys2cy3"
            # Add more intent-URL mappings here
        }
        
        if intent in url_mapping:
            url = url_mapping[intent]
            dispatcher.utter_message(text=f"Sure! Opening {url}?")
            
            webbrowser.open_new_tab(url)
            # Set a slot to store the URL
            return [SlotSet("navigated_url", url)]
        else:
            dispatcher.utter_message(text="I'm sorry, I don't know where to navigate.")
        
        return []

