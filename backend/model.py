from dotenv import load_dotenv
from promptSystemInstructions import SystemInstructions
from YouTubeTranscripts import YouTubeTranscripts
import os
import google.generativeai as genai

load_dotenv()
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

chat_session = model.start_chat(
  history=[
  ]
)

url_video_Youtube = str(input("Inserivi il link del video Youtube-> "))
response = chat_session.send_message(YouTubeTranscripts(url_video_Youtube))
print(f"ChatAI: {response.text}")

while True:
    user_input = str(input("-> "))
    response = chat_session.send_message(user_input)

    print(f"ChatAI: {response.text}")