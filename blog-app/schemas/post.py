from typing import Annotated, Optional

from schemas.user import UserRead
from pydantic import BaseModel, Field


class PostBase(BaseModel):
    title: str
    body: str


class PostCreate(PostBase):
    user_id: int


class PostRead(PostBase):
    id: int = Field(example=42)
    author: UserRead

