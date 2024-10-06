import asyncio

import structlog
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from backend.database import Base, engine
from backend.middleware.logger_middleware import logger_middleware
from backend.services.NotificationService import run_every_hour
from backend.utils.utils import create_app, write_openapi

Base.metadata.create_all(bind=engine)

app = create_app()
logger = structlog.get_logger()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(logger_middleware)

write_openapi()


@app.on_event("startup")
def start_hourly_task():
    asyncio.create_task(run_every_hour())


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
