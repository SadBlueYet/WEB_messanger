import logging
from typing import ClassVar

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine, AsyncEngine


load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    class DB(BaseSettings):
        POSTGRES_HOST: str = "localhost"
        POSTGRES_PORT: int = 5432
        POSTGRES_USER: str = "postgres"
        POSTGRES_PASSWORD: str = "1"
        POSTGRES_DB: str = "postgres"
        SCHEMA_CONTENT: str = "public"

        @property
        def POSTGRES_DSN(self) -> str:
            return (
                f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
            )



    class Logging:
        LOG_LEVEL: str = "INFO"
        LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    model_config = SettingsConfigDict(case_sensitive=True)

    def setup_logging(self):
        logging.basicConfig(level=self.Logging.LOG_LEVEL, format=self.Logging.LOG_FORMAT)

    LOGGING: ClassVar[Logging] = Logging()
    DATABASES: ClassVar[DB] = DB()

    engine: AsyncEngine = create_async_engine(DATABASES.POSTGRES_DSN)
    async_session_maker: async_sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    async def get_async_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.async_session_maker() as session:
            yield session

settings = Settings()
settings.setup_logging()
