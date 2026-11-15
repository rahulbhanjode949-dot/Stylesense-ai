import streamlit as st
from google import genai

st.set_page_config(page_title="StyleSense AI", page_icon="👔")
st.title("👔 StyleSense AI Stylist")
st.caption("Your personal grooming & outfit advisor")

# (तुमची Gemini API Key इथे टाका / Paste your API key here)
API_KEY = "YOUR_API_KEY_HERE"
client = genai.Client(api_key=API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hey! Tell me your height, skin tone, or occasion—I'll build your look."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if user_prompt := st.chat_input("Ask about outfits, hairstyle, or budget..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

    stylist_instruction = (
        "You are StyleSense AI, a sharp personal fashion and grooming stylist for Indian men. "
        "Give practical, direct outfit color combinations, hairstyles, and budget advice in simple English. "
        "Keep answers concise and actionable."
    )

    with st.chat_message("assistant"):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{stylist_instruction}\n\nUser asks: {user_prompt}"
        )
        st.write(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
      
