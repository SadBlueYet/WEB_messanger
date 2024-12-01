import logging
from typing import ClassVar

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from collections.abc import AsyncGenerator



load_dotenv(find_dotenv(".env"))

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

        def setup_logging(self):
            logging.basicConfig(level=self.Logging.LOG_LEVEL, format=self.Logging.LOG_FORMAT)


class AccessToken(BaseSettings):
    LIFETIME_SECONDS: int = 3600


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    LOGGING: ClassVar[Logging] = Logging()
    DATABASES: ClassVar[DB] = DB()
    ACCEES_TOKEN: ClassVar[AccessToken] = AccessToken()


settings = Settings()
settings.LOGGING.setup_logging()
