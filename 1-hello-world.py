from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
google_key = os.getenv('GOOGLE_API_KEY')
openai_key = os.getenv('OPENAI_API_KEY')
model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
message = model.invoke("Hello")
print(message)
