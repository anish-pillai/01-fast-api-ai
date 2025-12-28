import os
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
def get_llm():
    # Load env (already called at import, but ensure it's present if .env changed)
    dotenv.load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Set the environment variable before running. "
            "For Docker: `docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -p 8000:8000 fastapi-ai`"
        )

    # Ensure the underlying OpenAI client can also pick it up from the process env
    os.environ.setdefault("OPENAI_API_KEY", api_key)

    return ChatOpenAI(
        api_key=api_key,
        model="gpt-4o-mini",
        streaming=True,
        temperature=0.7,
    )