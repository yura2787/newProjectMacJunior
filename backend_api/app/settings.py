from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    POSTGRES_HOST: str

    DEBUG: bool = False

    JWT_SECRET: str
    JWT_ALGORITHM: str

    RMQ_HOST: str
    RMQ_PORT: int
    RMQ_VIRTUAL_HOST: str
    RMQ_USER: str
    RMQ_PASSWORD : str


    ACCESS_KEY: str
    SECRET_KEY: str
    BUCKET_NAME: str
    ENDPOINT: str
    PUBLIC_URL: str


    SENTRY: str

    @property
    def DATABASE_URL_ASYNC(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
