from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.posts.crud import PostCRUD
from models.db import async_session


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
        await session.close()

def post_crud(
    session: Annotated[
        AsyncSession,
        Depends(get_async_session),
    ],
) -> PostCRUD:
    return PostCRUD(session)


