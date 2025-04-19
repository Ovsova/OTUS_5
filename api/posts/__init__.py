from fastapi import APIRouter

from api.posts.views import router as posts_router

router = APIRouter(
    prefix="/posts",
    tags=["POSTS"],
)
router.include_router(posts_router)