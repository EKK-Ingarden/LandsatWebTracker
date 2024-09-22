from supabase import Client, create_client

from backend.settings import settings

supabase: Client = create_client(settings.supabase_url, settings.supabase_key)
