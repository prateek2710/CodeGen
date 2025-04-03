import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

class Chatbot:
    def __init__(self):
        self.conversation_history = []

    def get_response(self, user_input):
        # Add user message to conversation history
        self.conversation_history.append({"role": "user", "content": user_input})

        try:
            # Get response from OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.conversation_history
            )

            # Extract assistant's response
            assistant_response = response.choices[0].message['content']
            
            # Add assistant's response to conversation history
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            
            return assistant_response

        except Exception as e:
            return f"An error occurred: {str(e)}"

    def clear_history(self):
        self.conversation_history = []
