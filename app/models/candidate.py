from datetime import datetime
from sqlalchemy import Datetime, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index = True,
    )