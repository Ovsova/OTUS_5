from fastapi import APIRouter

from blog_app.api.users import router as api_user
from blog_app.api.posts import router as api_posts


router = APIRouter(
    prefix="/api",
    tags=["API"],
)

router.include_router(api_user)
router.include_router(api_posts)
