from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Usage(Base):
    __tablename__ = "usage"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

    chat_id: Mapped[UUID] = mapped_column(
        ForeignKey("chats.id", ondelete="CASCADE"),
        nullable=False,
    )

    prompt_tokens: Mapped[int] = mapped_column(Integer, nullable=False)
    completion_tokens: Mapped[int] = mapped_column(Integer, nullable=False)
    total_tokens: Mapped[int] = mapped_column(Integer, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        default=datetime.utcnow,
        nullable=False,
    )