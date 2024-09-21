from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost:5432/landsat_web_tracker_db"
    landsat_provider_url: str = "https://planetarycomputer.microsoft.com/api/stac/v1"

    model_config = SettingsConfigDict(env_file=(".env", ".env.production"))


settings = Settings()
