from typing import Annotated, Optional

from .user import UserRead
from pydantic import BaseModel, Field

import os
print("Текущая рабочая директория:", os.getcwd())

class PostBase(BaseModel):
    title: str
    body: str


class PostCreate(PostBase):
    user_id: int


class PostRead(PostBase):
    id: int = Field(example=42)
    author: UserRead

