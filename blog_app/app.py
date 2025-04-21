from fastapi import FastAPI, APIRouter, Depends
from typing import Annotated
from .create_fastapi_app import create_app
from blog_app.api import router as api_router
from blog_app.api.users.dependencies import users_crud, UsersCRUD
from blog_app.schemas import UserRead

app: FastAPI = create_app(
    create_custom_static_urls=True,
)
app.include_router(api_router)
default_router = APIRouter()

@default_router.get(
    "/",
    response_model=list[UserRead],
)
async def get_users(
    crud: Annotated[UsersCRUD, Depends(users_crud)],
):
    return await crud.get()

app.include_router(default_router)

