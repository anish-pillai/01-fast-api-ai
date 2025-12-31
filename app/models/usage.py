from datetime import datetime
from uuid import UUID, uuid4
import uuid

from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa
from app.db.base import Base


class Usage(Base):
    __tablename__ = "usage"

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
    prompt_tokens = sa.Column(sa.Integer(), nullable=False)
    completion_tokens = sa.Column(sa.Integer(), nullable=False)
    total_tokens = sa.Column(sa.Integer(), nullable=False)
    created_at = sa.Column(
        sa.DateTime(timezone=True),
        server_default=sa.func.now(),
        nullable=False
    )