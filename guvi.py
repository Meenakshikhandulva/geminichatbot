import streamlit as st
import google.generativeai as genai


st.title("welcome to gemini chat")

genai.configure(api_key="AIzaSyADn91ZpBQQQTqZzAGmmgMKkzi1j1z6A40")

text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)