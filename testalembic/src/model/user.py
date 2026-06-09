from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from src.db.db_config import Base


class User(Base):
    __tablename__ = 'user'
    id = mapped_column(Integer,primary_key=True)
    name = mapped_column(String(100),nullable=False)