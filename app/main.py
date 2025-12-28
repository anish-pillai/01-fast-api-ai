from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain_core.messages import HumanMessage
from app.graph import build_graph
from app.schemas import ChatRequest
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
graph = build_graph()

async def stream_chat(message: str):
    inputs = {
        "messages": [HumanMessage(content=message)]
    }

    async for event in graph.astream_events(inputs, version="v1"):
        if event["event"] == "on_chat_model_stream":
            token = event["data"]["chunk"].content
            if token:
                yield token
                await asyncio.sleep(0)  # yield control


@app.post("/chat")
async def chat(request: ChatRequest):
    return StreamingResponse(
        stream_chat(request.message),
        media_type="text/plain"
    )