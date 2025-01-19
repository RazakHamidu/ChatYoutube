from model import model
import streamlit as st  

st.title("💬 ChatYoutube")

input_container = st.empty()

url_video_Youtube = input_container.text_input("",placeholder="Inserisci in link del video Youtube")


if url_video_Youtube:
    input_container.empty()

    st.video(url_video_Youtube)

    with st.container(border=True):
        st.markdown(model(url_video_Youtube=url_video_Youtube))

    url_video_Youtube = st.empty()
    url_video_Youtube.empty() 
