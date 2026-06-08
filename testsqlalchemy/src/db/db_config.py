from sqlalchemy import create_engine, DateTime, func
from dotenv import load_dotenv
import os

from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

load_dotenv()

engine = create_engine(os.getenv("DB_URL"),echo=True)

SessionLocal =  sessionmaker(bind=engine,
             autocommit=False,
             autoflush=False,)

class Base(DeclarativeBase):
   created_at:Mapped[DateTime] = mapped_column(DateTime,default=func.now(),nullable=False)
   updated_at:Mapped[DateTime] = mapped_column(DateTime,default=func.now(),
                                               onupdate=func.now())




