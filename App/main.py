from model import model  # Importa la funzione principale per generare riassunti
import streamlit as st  # Libreria per creare interfacce utente web interattive

# Imposta il titolo dell'app
st.title("💬 SumTube")

# Crea un contenitore vuoto per l'input
input_container = st.empty()

# Crea una casella di testo per inserire il link del video YouTube
url_video_Youtube = input_container.text_input("", placeholder="Inserisci in link del video Youtube")

# Verifica se l'utente ha inserito un URL
if url_video_Youtube:
    input_container.empty()  # Svuota il contenitore dell'input per pulizia

    st.video(url_video_Youtube)  # Mostra il video di YouTube nell'app

    # Crea un contenitore per visualizzare il riassunto del video
    with st.container():
        st.markdown(model(url_video_Youtube=url_video_Youtube))  # Chiama la funzione `model` per generare il riassunto

    # Resetta il contenitore dell'URL per evitare confusione
    url_video_Youtube = st.empty()
    url_video_Youtube.empty()
