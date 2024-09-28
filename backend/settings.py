from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost:5432/landsat_web_tracker_db"
    landsat_provider_url: str = "https://planetarycomputer.microsoft.com/api/stac/v1"
    usgs_m2m_api_key: str = "<api key>"
    nuxt_open_fetch_api_base_url: str = "http://localhost:8000"
    supabase_url: str = "https://<id>.supabase.co"
    supabase_key: str = "<secret key>"

    model_config = SettingsConfigDict(env_file=(".env", ".env.production"))


settings = Settings()
