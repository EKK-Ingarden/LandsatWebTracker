from typing import List

import structlog
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend import models, schemas
from backend.database import get_db
from backend.utils.auth import get_current_user

logger = structlog.get_logger()

auth_router = APIRouter()


@auth_router.get("/get_user", description="Returns Supabase user information")
async def get_user(user: dict = Depends(get_current_user)):
    return user


@auth_router.get("/get_users", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
