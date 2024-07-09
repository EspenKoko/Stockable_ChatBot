from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class DefaultFallbackAction(Action):
    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        # Your default response message
        response = "I'm sorry, I couldn't understand your question. Can you please rephrase or ask something else?"

        # Send the default response to the user
        dispatcher.utter_message(response)

        # Return a SlotSet event to indicate that the fallback action was triggered
        return [SlotSet("fallback_triggered", True)]

# from flask import Flask
# from flask_cors import CORS
# from rasa import run

# # Initialize the Flask app
# app = Flask(__name__)

# # Enable CORS
# CORS(app)

# # Define the Rasa API route
# @app.route('/webhooks/rest/webhook', methods=['POST'])
# def rasa_webhook():
#     # Call the Rasa run function
#     return run()

# if __name__ == '__main__':
#     # Run the Flask app
#     app.run(debug=True, port=5005)
