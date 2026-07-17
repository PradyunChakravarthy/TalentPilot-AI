import os
import fitz
from fastapi import UploadFile


class PDFService:
    UPLOAD_DIR = "uploads"

    def __init__(self):
        os.makedirs(self.UPLOAD_DIR, exist_ok=True)

    async def extract_text(self, file: UploadFile) -> tuple[str, str]:
        file_path = os.path.join(self.UPLOAD_DIR, file.filename)

        contents = await file.read()

        with open(file_path, "wb") as f:
            f.write(contents)

        document = fitz.open(file_path)

        text = ""
        for page in document:
            text += page.get_text()

        document.close()

        return file.filename, text