# app.py
import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from VideoSection import VideoSection
# Configurazione Streamlit
st.title("💬 ChatYoutube")


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Configurazione del modello
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
    model_name="gemini-exp-1206",
    generation_config=generation_config,
)


# Stato della sessione per la chat
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.messages = []

# Visualizza i messaggi della conversazione
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input dell'utente
if user_input := st.chat_input("Scrivi il tuo messaggio:"):
    # Aggiungi input dell'utente allo stato della sessione
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Invia il messaggio a Gemini e ottieni la risposta
    response = st.session_state.chat_session.send_message(user_input)
    bot_response = response.text
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.chat_message("assistant").write(bot_response)

