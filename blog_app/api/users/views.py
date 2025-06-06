from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends

from pydantic import PositiveInt

from blog_app.schemas import UserRead, UserCreate, PostRead, PostCreate
from blog_app.models import User, Post
from .crud import UsersCRUD
from .dependencies import get_user_by_token, users_crud


router = APIRouter()


@router.get(
    "/",
    response_model=list[UserRead],
)
async def get_users(
    crud: Annotated[UsersCRUD, Depends(users_crud)],
) -> list[User]:
    return await crud.get()


@router.post(
    "/",
    response_model=UserRead,
)
async def create_user(
    user_in: UserCreate,
    crud: Annotated[UsersCRUD, Depends(users_crud)],
) -> User:
    return await crud.create(user_in=user_in)


@router.get(
    "/me",
    response_model=UserRead,
)
def get_me(
    user: Annotated[User, Depends(get_user_by_token)],
):
    return user


@router.get(
    "/{user_id}",
    response_model=UserRead,
)
async def get_user(
    user_id: PositiveInt,
    crud: Annotated[UsersCRUD, Depends(users_crud)],
) -> User:
    user = await crud.get_by_id(user_id=user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )