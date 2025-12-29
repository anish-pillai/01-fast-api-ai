from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Text, DateTime, ForeignKey, Integer
from datetime import datetime
from uuid import UUID, uuid4

class Base(DeclarativeBase):
    pass


class Chat(Base):
    __tablename__ = "chats"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    chat_id: Mapped[UUID] = mapped_column(ForeignKey("chats.id"))
    role: Mapped[str]  # user | assistant
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)


class Usage(Base):
    __tablename__ = "usage"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    chat_id: Mapped[UUID]
    prompt_tokens: Mapped[int] = mapped_column(Integer)
    completion_tokens: Mapped[int] = mapped_column(Integer)
    total_tokens: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)