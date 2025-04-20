from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from schemas import PostCreate
from models import Post


class PostCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self) -> list[Post]:
        statement = select(Post).options(selectinload(Post.author)).order_by(Post.id)
        result = await self.session.execute(statement)
        return list(result.scalars().all())

    async def get_by_id(self, post_id: int) -> Post | None:
        statement = select(Post).options(selectinload(Post.author)).where(Post.id == post_id)
        result = await self.session.execute(statement)
        post = result.scalar_one_or_none()
        if post and not post.author:
            await self.session.refresh(post, ["author"])
        return post

    async def create(self, post_in: PostCreate) -> Post:
        post = Post(title=post_in.title,
                body=post_in.body,
                user_id=post_in.user_id
    )
        self.session.add(post)
        await self.session.commit()
        await self.session.refresh(post)
        await self.session.refresh(post, ['author'])
        return post
