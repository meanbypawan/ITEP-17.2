from sqlalchemy import Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class Book(Base):
    __tablename__ = 'book'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String(100),nullable=False)
    price:Mapped[float] = mapped_column(Numeric(11,2),nullable=False)
    published_year:Mapped[int] = mapped_column(Integer,nullable=False)
    author_id:Mapped[int] = mapped_column(Integer,ForeignKey('author.id'),nullable=False)

    author:Mapped["Author"] = relationship("Author",
                                           back_populates="books")