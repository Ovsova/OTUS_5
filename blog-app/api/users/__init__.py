from fastapi import APIRouter

from api.users.views import router as users_router

router = APIRouter(
    prefix="/users",
    tags=["USERS"],
)
router.include_router(users_router)