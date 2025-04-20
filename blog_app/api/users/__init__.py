from fastapi import APIRouter

from blog_app.api.users.views import router as users_router

router = APIRouter(
    prefix="/users",
    tags=["USERS"],
)
router.include_router(users_router)