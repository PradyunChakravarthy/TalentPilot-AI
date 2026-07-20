from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.candidate import Candidate
from app.llm.schemas import CandidateExtraction

class CandidateRepository:
    def __init__(self, db:AsyncSession):
        self.db = db
    
    async def get_by_email(self, email:str):
        result = await self.db.execute(
            select(Candidate).where(Candidate.email == email)
        )
        return result.scalar_one_or_none()
    
    async def create(self, candidate: CandidateExtraction):
        db_candidate = Candidate(
          full_name=candidate.full_name,
            email=candidate.email,
            phone=candidate.phone,
            skills=",".join(candidate.skills),
            education=",".join(candidate.education),
            experience_years=candidate.experience_years,
            projects=",".join(candidate.projects),
        )
        self.db.add(db_candidate)
        await self.db.commit()
        await self.db.refresh(db_candidate)
        return db_candidate
        
    async def get_all(self):
        result = await self.db.execute(select(Candidate))
        return result.scalars().all()
        