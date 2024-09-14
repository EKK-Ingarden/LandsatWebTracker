import uuid
import structlog
from fastapi import FastAPI, Request, Response

from backend.src.middleware import logger_middleware
from backend.src.routers import index_router, coordinates_router
import uvicorn

if __name__ == '__main__':
    app = FastAPI()
    logger = structlog.get_logger()

    app.middleware("http")(logger_middleware)

    app.include_router(index_router,        prefix="")
    app.include_router(coordinates_router,  prefix="/coordinates")


    uvicorn.run(app, host="localhost", port=8000)