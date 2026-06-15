from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('mysql+pymysql://root:Root#123@localhost:3306/universitydb',echo=True)

SessionLocal = sessionmaker(bind=engine,
             autocommit=False,
             autoflush=False,)
class Base(DeclarativeBase):
    pass