from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate

class UserSService:
    
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register_user(self, user: UserCreate):

        existing = await self.repository.get_by_email(user.email)
        if existing:
            raise ValueError("User with this email already exists")
        
        return await self.repository.create(user)