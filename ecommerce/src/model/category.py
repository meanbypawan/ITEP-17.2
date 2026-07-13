from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base

class Category(Base):
    __tablename__ = 'category'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    category_name:Mapped[str] = mapped_column(String(100),unique=True)
    category_image:Mapped[str] = mapped_column(String(100))

    products:Mapped[list["Product"]] = relationship("Product",
                                                    back_populates="category",
                                                    cascade="all, delete-orphan")
