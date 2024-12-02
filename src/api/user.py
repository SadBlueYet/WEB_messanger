from fastapi import APIRouter

from .fastapi_users_router import fastapi_users
from config import settings
from schemas.user import (
    UserRead,
    UserUpdate,
)

router = APIRouter(
    prefix=f"/api{settings.API.v1.users}",
    tags=["Users"],
)

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)