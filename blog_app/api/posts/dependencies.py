from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from blog_app.api.posts.crud import PostCRUD
from blog_app.models.db import async_session


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()

def post_crud(
    session: Annotated[
        AsyncSession,
        Depends(get_async_session),
    ],
) -> PostCRUD:
    return PostCRUD(session)


