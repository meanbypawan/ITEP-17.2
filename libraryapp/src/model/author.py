from sqlalchemy import Integer, String

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base

class Author(Base):
    __tablename__ = 'author'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    email:Mapped[str] = mapped_column(String(100),unique=True,nullable=False,index=True)
    country:Mapped[str] = mapped_column(String(100),nullable=False)

    books:Mapped[list["Book"]] = relationship("Book",
                                              cascade="all,delete-orphan",
                                              back_populates="author")

