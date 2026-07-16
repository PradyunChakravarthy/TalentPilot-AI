from fastapi import APIRouter
from datetime import datetime
from app.core.config import get_settings

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

settings = get_settings()

@router.get("/")
def health():

    return {

        "status": "healthy",

        "application": settings.APP_NAME,

        "version": settings.APP_VERSION,

        "timestamp": datetime.now().isoformat(),

        "environment": "development",

    }