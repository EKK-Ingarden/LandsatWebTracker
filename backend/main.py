import structlog
import uvicorn
from backend.database import Base, engine
from backend.middleware.logger_middleware import logger_middleware
from backend.utils.utils import create_app, write_openapi
from fastapi.middleware.cors import CORSMiddleware

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

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
