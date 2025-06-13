from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/avgdb"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_= AsyncSession, expires_on_commit = True)
Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session