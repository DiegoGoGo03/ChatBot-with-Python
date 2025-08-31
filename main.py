import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

# ----- CONFIGURACIÓN -----
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="ChatBot con Python", page_icon="🤖", layout="centered")

# ----- ENCABEZADO CON PORTAFOLIO -----

st.markdown(
    """
    <div style='display: flex; justify-content: space-between; align-items: center;'>
        <h2>🤖 ChatBot con Python y Gemini</h2>
        <a href="https://diego-felipe-gomez.netlify.app/" target="_blank" 
           style="text-decoration: none; background-color: #4CAF50; color: white; 
                  padding: 8px 16px; border-radius: 8px; font-weight: bold;">
            &lt;KRESTO_DEV&gt;
        </a>
    </div>
    <hr>
    """,
    unsafe_allow_html=True
)

# ----- HISTORIAL -----
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----- RESPUESTA DEL BOT -----
def chatbot_response(user_input):
    chat = model.start_chat(history=st.session_state.messages)
    response = chat.send_message(user_input)
    return response.text

# ----- MOSTRAR CONVERSACIÓN -----
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div style='background:#DCF8C6;padding:10px;border-radius:10px;margin:5px;text-align:right;'>{msg['parts'][0]['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background:#E9E9EB;padding:10px;border-radius:10px;margin:5px;text-align:left;'>{msg['parts'][0]['text']}</div>", unsafe_allow_html=True)

# ----- INPUT DEL USUARIO -----
user_input = st.text_input("Escribe tu mensaje:", "")

if st.button("Enviar") and user_input.strip() != "":
    st.session_state.messages.append({"role": "user", "parts": [{"text": user_input}]})
    respuesta = chatbot_response(user_input)
    st.session_state.messages.append({"role": "model", "parts": [{"text": respuesta}]})
    st.rerun()

