import os
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

def get_llm():
    return ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-4o-mini",
        streaming=True,
        temperature=0.7,
    )