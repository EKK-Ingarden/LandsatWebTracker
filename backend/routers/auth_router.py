
import structlog
from fastapi import APIRouter, Depends

from backend.utils.auth import get_current_user

logger = structlog.get_logger()

auth_router = APIRouter()


@auth_router.get("/get_user", description="Returns Supabase user information")
async def get_user(user: dict = Depends(get_current_user)):
    return user
