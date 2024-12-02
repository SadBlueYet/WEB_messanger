from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
    AsyncEngine,
)

from config import settings


class DataBaseHelper:
    async def get_async_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.async_session_maker() as session:
            yield session

    engine: AsyncEngine = create_async_engine(settings.DATABASES.POSTGRES_DSN)
    async_session_maker: async_sessionmaker = async_sessionmaker(
        engine, expire_on_commit=False
    )


db_helper = DataBaseHelper()
