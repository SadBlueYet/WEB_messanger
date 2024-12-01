from typing import (
    TYPE_CHECKING,
    Annotated,
)

from fastapi import Depends

from models import AccessToken
from config import settings


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_tokens_db(
    session: Annotated[
        "AsyncSession",
        Depends(settings.DATABASES.get_async_session),
    ],
):
    yield AccessToken.get_db(sescresion=session)