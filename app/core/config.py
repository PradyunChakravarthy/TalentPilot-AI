from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "TalentPilot API"

    APP_VERSION: str ="0.1.0"

    DEBUG: bool = False

    DATABASE_URL: str 

    JWT_SECRET_KEY: str 

    LLM_PROVIDER: str 

    GROQ_API_KEY: str 

    LLM_MODEL: str = "llama-3.3-70b-versatile"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra = "ignore",
        case_sensitive=True,
    )


@lru_cache
def get_settings():
    return Settings()