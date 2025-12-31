import uuid
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa
from app.db.base import Base

class Chat(Base):
    __tablename__ = "chats"

    id = sa.Column(sa.UUID(), primary_key=True)
    created_at = sa.Column(sa.DateTime(), nullable=False)