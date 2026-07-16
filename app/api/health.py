from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("")
def health_check():
    return {
        "status": "healthy, up and running",
        "application": "TalentPilot AI",
        "version": "0.1.0",
        "timestamp": datetime.utcnow().isoformat()
    }