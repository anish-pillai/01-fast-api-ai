from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

# 🔥 IMPORT MODELS HERE
from app.models.chat import Chat
from app.models.message import Message
from app.models.usage import Usage