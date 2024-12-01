from typing import (
    TYPE_CHECKING,
    Annotated,
)

from fastapi import Depends

from models import User
from db import db_helper

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_users_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.get_async_session),
    ],
):
    yield User.get_db(session=session)
