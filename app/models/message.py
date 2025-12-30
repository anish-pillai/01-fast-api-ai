from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, DateTime, ForeignKey, Integer
from datetime import datetime
from uuid import UUID, uuid4

from app.db.base import Base

class Message(Base):
    __tablename__ = "messages"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    chat_id: Mapped[UUID] = mapped_column(ForeignKey("chats.id"))
    role: Mapped[str]  # user | assistant
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)