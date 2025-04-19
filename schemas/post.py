from typing import Annotated, Optional

from schemas.user import UserRead
from pydantic import BaseModel, Field


class PostBase(BaseModel):
    title: str
    body: str


class PostCreate(PostBase):
    """
    Create post
    """
    user_id: int

class PostRead(PostBase):
    """
    Read post
    """
    id: int = Field(example=42)
    author: Optional[UserRead] = None

