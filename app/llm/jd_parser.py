from app.llm.client import llm
from app.schemas.job_description import JobDescription

structured_llm = llm.with_structured_output(JobDescription)

async def parse_jd(text: str) -> JobDescription:
    prompt = f"""
Extract the following information from the job description.

Return:
- title
- required_skills
- preferred_skills
- minimum_experience
- responsibilities

Job Description:
{text}
"""

    return await structured_llm.ainvoke(prompt)