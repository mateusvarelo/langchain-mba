from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

gemini = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai", temperature=0.5)
answer_gemini = gemini.invoke("Hello from Gemini")
print("Gemini Response:", answer_gemini.content)
