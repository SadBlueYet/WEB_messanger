import datetime
from http.client import HTTPException
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from .fastapi_users_router import fastapi_users
from db import db_helper
from authentication.backend import authentication_backend
from config import settings
from schemas.user import (
    UserRead,
    UserCreate,
)
from sqlalchemy import text

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

@router.patch("/refresh")
async def refresh_token(
        token: str,
        session: Annotated[
                AsyncSession,
                Depends(db_helper.get_async_session),
            ]
) -> dict:
    stmt = "UPDATE accesstoken SET created_at = :created_at WHERE token= :token"
    await session.execute(text(stmt), {"token": token, "created_at": datetime.datetime.now()})
    await session.commit()
    return {"message": "Token refreshed successfully", "token": token}
