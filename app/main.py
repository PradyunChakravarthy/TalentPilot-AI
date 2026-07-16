from fastapi import FastAPI
from app.core.config import get_settings
from app.api.health import router as health_router
settings =  get_settings()

def create_app()-> FastAPI:

    app = FastAPI(
    title = settings.APP_NAME,
    version = settings.APP_VERSION,
    debug = settings.DEBUG,
    )
    app.include_router(health_router)
    return app

app = create_app()