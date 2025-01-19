from langchain_community.document_loaders import YoutubeLoader  # Libreria per caricare trascrizioni da YouTube

# Funzione per ottenere le trascrizioni di un video YouTube
def YouTubeTranscripts(urlVideoYuotubr):
    # Crea un'istanza del loader con la lingua desiderata
    loader = YoutubeLoader.from_youtube_url(urlVideoYuotubr, language=["en", "it"])

    # Carica le trascrizioni dal video
    documents = loader.load()

    # Restituisce il contenuto della trascrizione del video
    for doc in documents: 
        return doc.page_content
