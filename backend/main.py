import structlog
import uvicorn
from backend.middleware import logger_middleware
from backend.routers import coordinates_router, index_router
from fastapi import FastAPI

app = FastAPI()
logger = structlog.get_logger()

app.middleware("http")(logger_middleware)

app.include_router(index_router,        prefix="")
app.include_router(coordinates_router,  prefix="/coordinates")

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
