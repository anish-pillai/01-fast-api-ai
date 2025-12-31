from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, DateTime, ForeignKey, Integer
from datetime import datetime
from uuid import UUID, uuid4
import sqlalchemy as sa
from app.db.base import Base

class Message(Base):
    __tablename__ = "messages"

    id = sa.Column(sa.UUID(), primary_key=True)
    chat_id = sa.Column(
        sa.UUID(),
        sa.ForeignKey("chats.id", ondelete="CASCADE"),
        nullable=False,
    )
    content = sa.Column(sa.Text(), nullable=False)
    created_at = sa.Column(sa.DateTime(), nullable=False)