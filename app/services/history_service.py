from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Chat, Message


async def get_chats(db: AsyncSession):
    stmt = (
        select(Chat)
        .order_by(Chat.created_at.desc())
        .limit(50)
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_messages_for_chat(
    db: AsyncSession,
    chat_id,
):
    stmt = (
        select(Message)
        .where(Message.chat_id == chat_id)
        .order_by(Message.created_at.asc())
    )
    result = await db.execute(stmt)
    return result.scalars().all()