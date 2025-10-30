import streamlit as st
from model import get_emotion, generate_response

st.set_page_config(page_title="AI Emotional Chatbot 🤖", page_icon="💬")

st.title("💬 AI Emotional Chatbot")
st.write("A Generative AI chatbot that understands your emotions and responds empathetically 💖")

user_input = st.text_input("Say something...")

if user_input:
    emotion = get_emotion(user_input)
    response = generate_response(user_input, emotion)
    st.markdown(f"**Emotion detected:** {emotion}")
    st.markdown(f"**Chatbot:** {response}")
