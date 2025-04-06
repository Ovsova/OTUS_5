from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base

if TYPE_CHECKING:
    from .user import User


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(
        String(140),
        default="",
        server_default="",
    )
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
    )

    author: Mapped["User"] = relationship(
        back_populates="posts",
    )

    def __str__(self):
        return self.title
