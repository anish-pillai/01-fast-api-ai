from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from langchain_core.messages import HumanMessage
from app.deps import get_db
from app.graph import build_graph
from app.schemas import (
    ChatRequest,
    ChatSummary,
    ChatHistoryResponse
)
from app.services.chat_service import create_chat, save_message
from app.services.history_service import (
    get_chats,
    get_messages_for_chat,
)
import asyncio
from dotenv import load_dotenv

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
async def chat(
    req: ChatRequest,
    db = Depends(get_db),
):
    chat = await create_chat(db)

    await save_message(
        db,
        chat_id=chat.id,
        role="user",
        content=req.message,
    )

    return {"chat_id": chat.id}

# List chats
@app.get("/chats", response_model=list[ChatSummary])
async def list_chats(
    db: AsyncSession = Depends(get_db),
):
    chats = await get_chats(db)
    return chats

# Fetch messages for a chat
@app.get(
    "/chats/{chat_id}/messages",
    response_model=ChatHistoryResponse,
)
async def chat_messages(
    chat_id,
    db: AsyncSession = Depends(get_db),
):
    messages = await get_messages_for_chat(db, chat_id)

    if not messages:
        raise HTTPException(status_code=404, detail="Chat not found")

    return {
        "chat_id": chat_id,
        "messages": messages,
    }