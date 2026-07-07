from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db_config import Base


class Admin(Base):
    __tablename__ = "admin"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    email:Mapped[str] = mapped_column(String(100),unique=True)
    password:Mapped[str] = mapped_column(String(100))

