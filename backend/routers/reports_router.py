import structlog
from fastapi import APIRouter

logger = structlog.get_logger()

reports_router = APIRouter()


@reports_router.get("/get_reports")
async def get_reports():
    raise NotImplementedError
