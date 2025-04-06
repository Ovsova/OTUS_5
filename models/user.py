from typing import TYPE_CHECKING
from sqlalchemy import (
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base

if TYPE_CHECKING:
    from .post import Post


class User(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(32))
    username: Mapped[str] = mapped_column(
        String(100), unique=True)
    email: Mapped[str | None] = mapped_column(String(120), unique=True)
    website: Mapped[str | None] = mapped_column(String(120))

    posts: Mapped[list["Post"]] = relationship(
        back_populates="author",
    )

    def __str__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, username={self.username!r}, email="
                f"{self.email!r}, website={self.website!r})")
