import streamlit as st  
from VideoSection import VideoSection

st.title("💬 ChatYoutube")


# https://youtu.be/CNsvts6pVzo?si=nEUDKEQhUu6xaBqL

# Contenitore vuoto per il text_input
input_container = st.empty()

# Mostra il campo di input
url_video_Youtube = input_container.text_input("",placeholder="Inserisci in link del video Youtube")


if url_video_Youtube:
    input_container.empty()
    VideoSection(url_video_Youtube)
    url_video_Youtube = st.empty()
    url_video_Youtube.empty() 

