from sqlalchemy.exc import IntegrityError
from sqlalchemy import (
    insert,
)
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.config import get_async_session
from app.database.models import Users


async def add_users(
        name: str,
        telegram_id: int,
        session: AsyncSession = Depends(
            get_async_session
        )
) -> bool:

    try:
        await session.execute(
            insert(Users).values(
                name=name,
                telegram_id=telegram_id
            )
        )
        await session.commit()
        return True

    except IntegrityError as ex:
        return False


