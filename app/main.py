from fastapi import FastAPI
from app.core.config import get_settings
from app.api.health import router as health_router
from app.db.init_db import init_db
from app.core.logger import setup_logger
from contextlib import asynccontextmanager

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
    return app

logger.info("TalentPilot API started successfully")
app = create_app()