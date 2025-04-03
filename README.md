# CodeGen - GenAI Powered Chatbot

A simple but powerful chatbot implementation using OpenAI's GPT-3.5-turbo model and Streamlit for the user interface.

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the Application

Run the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your default web browser.

## Features

- Interactive chat interface
- Conversation history
- Clear chat functionality
- Powered by GPT-3.5-turbo
