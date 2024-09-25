
import structlog
from fastapi import APIRouter, Response

logger = structlog.get_logger()

index_router = APIRouter()


@index_router.get("/healthcheck")
async def healthcheck():
    return Response()


@index_router.get("/")
async def read_main():
    logger.info("In root path")
    return {"msg": "Hello World"}
