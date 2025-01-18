from dotenv import load_dotenv
from promptSystemInstructions import SystemInstructions
import os
import google.generativeai as genai
from langchain_community.document_loaders import YoutubeLoader


InputYoutubeUrl = str(input("Insert url video -> "))
loader = YoutubeLoader.from_youtube_url(
    InputYoutubeUrl, add_video_info=False
)

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

while True:
    user_input = str(input("-> "))
    response = chat_session.send_message(user_input)

    print(f"ChatAI: {response.text}")