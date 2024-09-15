from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost:5432/landsat_web_tracker_dba"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
