from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = ""

    APP_VERSION: str =""

    DEBUG: bool = True

    DATABASE_URL: str = ""

    JWT_SECRET_KEY: str = ""

    LLM_PROVIDER: str = ""

    GROQ_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


@lru_cache
def get_settings():
    return Settings()