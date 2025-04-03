import streamlit as st
from chatbot import Chatbot

# Initialize session state
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = Chatbot()

st.title("GenAI Powered Chatbot")

# Add a clear chat button
if st.button("Clear Chat"):
    st.session_state.chatbot.clear_history()
    st.session_state.messages = []

# Initialize chat message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's on your mind?"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get and display assistant response
    with st.chat_message("assistant"):
        response = st.session_state.chatbot.get_response(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
