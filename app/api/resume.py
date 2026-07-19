from fastapi import APIRouter, File, HTTPException, UploadFile
from app.services.pdf_service import PDFService
from app.llm.resume_parser import parse_resume 
router = APIRouter()

pdf_service = PDFService()

@router.post("/upload")
async def upload_resume(file:UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    filename, text = await pdf_service.extract_text(file)
    
    candidate = await parse_resume(text)

    return candidate.model_dump()