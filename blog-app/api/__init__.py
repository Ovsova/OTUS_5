from fastapi import APIRouter

from api.users import router as api_user
from api.posts import router as api_posts


router = APIRouter(
    prefix="/api",
    tags=["API"],
)

router.include_router(api_user)
router.include_router(api_posts)
