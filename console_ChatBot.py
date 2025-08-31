import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
import random

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  

model = genai.GenerativeModel("gemini-1.5-flash")

print("Hola mundo")
print("En que podría ayudarte")
print("Escribe 'Salir' para salir")

chat = model.start_chat(history=[])
user_name = input("¿Cuál es tu nombre? ")

#Bucle infinito
while True:
  user_input = input(f"Hola {user_name} dime que deseas: ")
  if user_input == "Salir":
    break
  try:
    response = chat.send_message(user_input)
    print("ChatBot: ", response.text)
  except Exception as e:
    print("El Chatbot no responde: Error al comunicarnos con la API de Gemini", e)


st.title("🤖 ChatBot con Python")
st.write("Chatea con tu asistente de IA")

user_input = st.text_input("Escribe tu mensaje:")
if st.button("Enviar"):
    st.write(f"Tú: {user_input}")
    st.write("Bot: Aquí va la respuesta de tu modelo IA")
  
