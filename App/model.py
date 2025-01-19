from promptSystemInstructions import SystemInstructions
from YouTubeTranscripts import YouTubeTranscripts
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv() 

def model(url_video_Youtube):
  genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

  # Create the model
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    system_instruction=SystemInstructions()
  )
  response = model.generate_content(YouTubeTranscripts(url_video_Youtube))
  return response.text