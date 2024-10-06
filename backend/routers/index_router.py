import resend
import structlog
from fastapi import APIRouter, Response

from backend.services.NotificationService import NotificationService
from backend.settings import settings

resend.api_key = settings.resend_api_key

logger = structlog.get_logger()

index_router = APIRouter()


@index_router.get("/healthcheck")
async def healthcheck():
    return Response()


@index_router.get("/email")
async def email():
    user = {
        "email": "ami.g.098765432@gmail.com",
    }
    message = {"coordinates": [50.90473781103003, 15.731811290627371], "time_left": "30 minutes"}

    NotificationService.sendEmailNotification(user, message)

    return Response()


@index_router.get("/")
async def root():
    return {"info": "Landsat Web Tracker API", "version": "Work In Progress :3"}
