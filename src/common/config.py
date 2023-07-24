from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ["get_settings"]


class Settings(BaseSettings):
    app_name: str = "For-Nursery"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
