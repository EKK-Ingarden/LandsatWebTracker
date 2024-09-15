import structlog
import uvicorn
from backend.database import Base, engine
from backend.middleware.logger_middleware import logger_middleware
from backend.routers.coordinates_router import coordinates_router
from backend.routers.index_router import index_router
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI()
logger = structlog.get_logger()

app.middleware("http")(logger_middleware)

app.include_router(index_router, prefix="")
app.include_router(coordinates_router, prefix="/coordinates")

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
