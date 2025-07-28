import streamlit as st
from chatbot import Chatbot

# Initialize the chatbot without passing 'vectorstore'
chatbot = Chatbot()

# Streamlit UI
st.title("Real-time Sensor Data Chatbot")
user_query = st.text_input("Enter your query:")

if st.button("Get Response"):
    response = chatbot.generate_response(user_query)
    st.write(response)
