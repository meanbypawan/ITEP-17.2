from sqlalchemy import Integer, String
from sqlalchemy.testing.schema import mapped_column

from src.db.db_config import Base


class Client(Base):
    __tablename__ = 'client'
    id = mapped_column(Integer,primary_key=True)
    client_name = mapped_column(String(100),nullable=False)