from fastapi import APIRouter

from blog_app.api.posts.views import router as posts_router

router = APIRouter(
    prefix="/posts",
    tags=["POSTS"],
)
router.include_router(posts_router)