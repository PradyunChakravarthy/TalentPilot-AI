from pydantic import BaseModel, EmailStr

class CandidateExtraction(BaseModel):
    full_name:str
    email:EmailStr
    phone:str
    skills:list[str]
    education: list[str]
    experience_years: int
    projects: list[str]