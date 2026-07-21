from fastapi import FastAPI
from app.core.config import get_settings
from app.api.health import router as health_router
from app.db.init_db import init_db
from app.core.logger import setup_logger
from contextlib import asynccontextmanager
from app.api.resume import router as resume_router
from app.api import job_description

logger = setup_logger()

settings =  get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

def create_app()-> FastAPI:

    app = FastAPI(
    title = settings.APP_NAME,
    version = settings.APP_VERSION,
    debug = settings.DEBUG,
    lifespan = lifespan
    )
    app.include_router(health_router)
    app.include_router(
        resume_router,
        prefix="/resume",
        tags=["Resume"]
    )
    app.include_router(
        job_description.router,
        prefix = "/job-description",
        tags = ["Job Descritption"],
    )
    return app

logger.info("TalentPilot API started successfully")
app = create_app()