from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db_config import Base


class ToDo(Base):
    __tablename__ = "todos"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String(100),nullable=False)
    priority:Mapped[str] = mapped_column(String(10),nullable=False)
    description:Mapped[str] = mapped_column(String(255),nullable=True)
