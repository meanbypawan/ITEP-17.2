from sqlalchemy import create_engine, DateTime,func
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

DB_URL = "mysql+pymysql://root:Root#123@localhost:3306/alchemydb"

engine = create_engine(DB_URL,echo=True)

SessionLocal =   sessionmaker(bind=engine,
             autocommit=False,
             autoflush=False)
class Base(DeclarativeBase):
  created_at:Mapped[DateTime] = mapped_column(DateTime,default=func.now())
  updated_at:Mapped[DateTime] = mapped_column(DateTime,default=func.now(),onupdate=func.now())
