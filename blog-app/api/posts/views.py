from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends

from pydantic import PositiveInt

from schemas import PostRead, PostCreate
from models import Post
from .crud import PostCRUD
from .dependencies import post_crud

router = APIRouter()


@router.get(
    "/",
    response_model=list[PostRead],
)
async def get_posts(
        crud: Annotated[PostCRUD, Depends(post_crud)],
) -> list[Post]:
    posts = await crud.get()
    return posts


@router.post(
    "/",
    response_model=PostRead,
)
async def create_post(
        post_in: PostCreate,
        crud: PostCRUD = Depends(post_crud),
) -> Post:
    try:
        post = await crud.create(post_in=post_in)
        return post
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get(
    "/{post_id}",
    response_model=PostRead,
)
async def get_post(
        post_id: PositiveInt,
        crud: Annotated[PostCRUD, Depends(post_crud)],
) -> Post:
    post = await crud.get_by_id(post_id=post_id)
    if not post:
        raise HTTPException(status_code=404)
    if not post.author:
        await crud.session.refresh(post, ["author"])
        if not post.author:
            raise HTTPException(
                status_code=500,
                detail=f"Author not loaded for post {post_id}"
            )

    return post