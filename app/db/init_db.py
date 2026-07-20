from app.db.base import Base
from app.db.database import engine

from app.models.users import User
from app.models.candidate import Candidate
async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

"""
Why import User if it's not used?

Base.metadata only knows about models that have been imported. Importing User registers it with SQLAlchemy, so create_all() knows which tables to create.
"""