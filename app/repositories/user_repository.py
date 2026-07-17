from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.users import User
from app.schemas.user import UserCreate 

class UserRepository:

    def __init__ (self, db: AsyncSession):
        self.db = db
    
    async def get_by_email(self, email:str):
        statement = select(User).where(User.email == email)
        result = await self.db.execute(statement)
        return result.scalar_one_or_none()
    
    async def create(self, user:UserCreate):

        db_user = User(
            full_name = user.full_name,
            email= user.email,
            hashed_password= user.password #Temporary
        )

        self.db.add(db_user)

        await self.db.commit()
        await self.db.refresh(db_user)
        
        return db_user
