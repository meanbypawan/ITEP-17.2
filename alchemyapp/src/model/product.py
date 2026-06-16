from sqlalchemy import Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db_config import Base


class Product(Base):
    __tablename__ = "product"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String(100),nullable=False)
    price:Mapped[float] = mapped_column(Numeric(10,2),nullable=False)
    brand:Mapped[str] = mapped_column(String(100),nullable=False)
    discount_percentage:Mapped[float] = mapped_column(Numeric(10,2))
    category_name:Mapped[str] = mapped_column(String(100),nullable=False)

    def __repr__(self):
        return f"Product : {self.id} : {self.title} : {self.price} : {self.brand}"