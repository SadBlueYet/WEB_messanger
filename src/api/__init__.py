from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.security import HTTPBearer

from config import settings

from .auth import router as auth_router
from .user import router as user_router

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=f"/api{settings.API.v1.prefix}",
    dependencies=[Depends(http_bearer)],
)
router.include_router(auth_router)
router.include_router(user_router)
