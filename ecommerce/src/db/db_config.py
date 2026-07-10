from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv
import os

from sqlalchemy.orm import DeclarativeBase

load_dotenv()

engine = create_async_engine(os.getenv("DB_URL",""),echo=True)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_session():
    async with SessionLocal.begin() as session:
        yield session



