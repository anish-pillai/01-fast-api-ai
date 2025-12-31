import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, DateTime, ForeignKey, Integer
from datetime import datetime
from uuid import UUID, uuid4
import sqlalchemy as sa
from app.db.base import Base

class Message(Base):
    __tablename__ = "messages"

    id = sa.Column(
        sa.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    chat_id = sa.Column(
        sa.UUID(),
        sa.ForeignKey("chats.id", ondelete="CASCADE"),
        nullable=False,
    )

    role = sa.Column(
        sa.String(length=20),
        nullable=False
    )
    
    content = sa.Column(sa.Text(), nullable=False)
    created_at = sa.Column(
        sa.DateTime(timezone=True),
        server_default=sa.func.now(),
        nullable=False
    )