from promptSystemInstructions import SystemInstructions  # Importa il prompt personalizzato per il modello AI
from YouTubeTranscripts import YouTubeTranscripts  # Importa la funzione per ottenere trascrizioni dai video
from dotenv import load_dotenv  # Libreria per caricare variabili di ambiente
import os  # Libreria standard per gestire file e percorsi
import google.generativeai as genai  # Libreria per utilizzare il modello Google Generative AI

# Carica le variabili di ambiente dal file `.env`
load_dotenv()

# Funzione principale per generare il riassunto
def model(url_video_Youtube):
    # Configura l'API di Google Generative AI con la chiave API
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Configurazione del modello generativo
    generation_config = {
        "temperature": 1,  # Controlla la casualità delle risposte
        "top_p": 0.95,  # Penalizza la probabilità di token rari
        "top_k": 40,  # Considera solo i top 40 token più probabili
        "max_output_tokens": 8192,  # Numero massimo di token generati
        "response_mime_type": "text/plain",  # Tipo di risposta testuale
    }

    # Crea un'istanza del modello con il prompt personalizzato
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
        system_instruction=SystemInstructions()
    )

    # Genera il contenuto basandosi sulle trascrizioni del video
    response = model.generate_content(YouTubeTranscripts(url_video_Youtube))
    return response.text  # Ritorna il testo generato
