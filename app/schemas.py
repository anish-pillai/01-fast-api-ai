from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import List

class ChatRequest(BaseModel):
    message: str

class ChatSummary(BaseModel):
    id: UUID
    created_at: datetime


class MessageResponse(BaseModel):
    id: UUID
    role: str
    content: str
    created_at: datetime


class ChatHistoryResponse(BaseModel):
    chat_id: UUID
    messages: List[MessageResponse]