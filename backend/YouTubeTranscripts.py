from langchain_community.document_loaders import YoutubeLoader

def YouTubeTranscripts(urlVideoYuotubr):
    loader = YoutubeLoader.from_youtube_url(urlVideoYuotubr)

    documents = loader.load()

    for doc in documents: 
        return doc.page_content
