from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy_serializer import SerializerMixin

DB_URL="mysql+pymysql://root:Root#123@localhost:3306/relationshipdb"

engine = create_engine(DB_URL,echo=True)

SessionLocal = sessionmaker(bind=engine,
                            autocommit=False,
                            autoflush=False,)

class Base(DeclarativeBase,SerializerMixin):
    pass

