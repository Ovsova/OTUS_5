from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Header, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from blog_app.api.users.crud import UsersCRUD
from blog_app.models import User
from blog_app.models.db import async_session


async def get_async_session() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        yield session


def users_crud(
    session: Annotated[
        AsyncSession,
        Depends(get_async_session),
    ],
) -> UsersCRUD:
    return UsersCRUD(session)


async def get_user_by_token(
    crud: Annotated[UsersCRUD, Depends(users_crud)],
    token: Annotated[str, Header(alias="x-auth-token")],
) -> User:
    user = await crud.get_by_token(token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid token",
    )