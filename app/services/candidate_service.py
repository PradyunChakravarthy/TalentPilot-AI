from app.repositories.candidate_repository import CandidateRepository
from app.llm.schemas import CandidateExtraction

class CandidateService:
    def __init__(self, repository: CandidateRepository):
        self.repository = repository

    async def create_candidate(self, candidate: CandidateExtraction):
        existing = await self.repository.get_by_email(candidate.email)

        if existing:
            return existing
        
        return await self.repository.create(candidate)
    
    async def get_all_candidates(self):
        return await self.repository.get_all()