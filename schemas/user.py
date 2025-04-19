from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: Annotated[str, Len(min_length=3, max_length=100)]
    email: EmailStr | None = None
    name: str = ""


class UserCreate(UserBase):
    website: str | None = None


class UserRead(UserBase):
    id: int = Field(example=42)

