from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
message = model.invoke("Hello")
print(message)
