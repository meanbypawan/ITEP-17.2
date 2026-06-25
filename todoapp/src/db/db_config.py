from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DB_URL = "mysql+aiomysql://root:Root#123@localhost:3306/todoapp"

engine = create_async_engine(DB_URL,echo=True)

SessionLocal = async_sessionmaker(bind=engine,
                                  expire_on_commit=False)

class Base(DeclarativeBase):
    pass