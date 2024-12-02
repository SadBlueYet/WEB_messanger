from http.client import HTTPException

from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError

from .fastapi_users_router import fastapi_users
from authentication.backend import authentication_backend
from config import settings
from schemas.user import (
    UserRead,
    UserCreate,
)

router = APIRouter(
    prefix=settings.API.v1.auth,
    tags=["Auth"],
)

# /login
# /logout
router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
        # requires_verification=True,
    ),
)


# /register
router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)

# /request-verify-token
# /verify
router.include_router(
    router=fastapi_users.get_verify_router(UserRead),
)

# /forgot-password
# /reset-password
router.include_router(
    router=fastapi_users.get_reset_password_router(),
)