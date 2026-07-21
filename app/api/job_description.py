from fastapi import APIRouter, File, HTTPException, UploadFile

from app.llm.jd_parser import parse_jd
from app.schemas.job_description import JobDescription
from app.services.pdf_service import PDFService

router = APIRouter()
pdf_service = PDFService()

@router.post("/upload", response_model=JobDescription)
async def upload_job_description(file: UploadFile = File(...)):
    try:
        _, text = await pdf_service.extract_text(file)
        jd = await parse_jd(text)
        return jd
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))