from backend.settings import settings
from supabase import Client, create_client

supabase: Client = create_client(settings.supabase_url, settings.supabase_key)
