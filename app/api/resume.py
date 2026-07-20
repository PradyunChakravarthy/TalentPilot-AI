from fastapi import APIRouter, File, HTTPException, UploadFile
from app.services.pdf_service import PDFService
from app.llm.resume_parser import parse_resume 
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.repositories.candidate_repository import CandidateRepository
from app.services.candidate_service import CandidateService

router = APIRouter()

pdf_service = PDFService()

@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    filename, text = await pdf_service.extract_text(file)

    candidate = await parse_resume(text)

    repository = CandidateRepository(db)
    service = CandidateService(repository)

    saved = await service.create_candidate(candidate)

    return {
        "message": "Candidate stored successfully",
        "candidate_id": saved.id,
    }

@router.get("/")
async def get_candidated(
    db: AsyncSession = Depends(get_db)
):
    repository = CandidateRepository(db)
    service = CandidateService(repository)

    candidates = await service.get_all_candidates()

    return candidates