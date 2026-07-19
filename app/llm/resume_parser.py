from app.llm.client import llm 
from app.llm.schemas import CandidateExtraction

structured_llm = llm.with_structured_output(CandidateExtraction)

async def parse_resume(text:str)-> CandidateExtraction:
    prompt = f"""
Extract candidate information from the following resume.

Resume:
{text}
"""
    return await structured_llm.ainvoke(prompt)
