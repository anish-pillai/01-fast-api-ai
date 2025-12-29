from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Chat, Message

async def create_chat(db: AsyncSession) -> Chat:
    chat = Chat()
    db.add(chat)
    await db.commit()
    await db.refresh(chat)
    return chat


async def save_message(
    db: AsyncSession,
    chat_id,
    role: str,
    content: str,
):
    msg = Message(
        chat_id=chat_id,
        role=role,
        content=content,
    )
    db.add(msg)
    await db.commit()