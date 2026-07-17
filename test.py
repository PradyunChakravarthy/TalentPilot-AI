from sqlalchemy.ext.asyncio import create_async_engine

url = "sqlite+aiosqlite:///./talentpilot.db"

print("Creating engine...")

engine = create_async_engine(url)

print("Success!")