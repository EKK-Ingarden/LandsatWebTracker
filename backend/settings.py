from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    landsat_provider_url: str = "https://planetarycomputer.microsoft.com/api/stac/v1"
    database_url: str = Field()
    supabase_url: str = Field()
    supabase_key: str = Field()
    resend_api_key: str = Field()

    model_config = SettingsConfigDict(env_file=(".env", ".env.production"), extra="ignore")


settings = Settings()
