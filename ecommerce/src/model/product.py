from sqlalchemy import Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class Product(Base):
    __tablename__ = 'product'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String(100))
    price:Mapped[float] = mapped_column(Numeric(10,2))
    description:Mapped[str] = mapped_column(String(500),nullable=True)
    warranty_information:Mapped[str] = mapped_column(String(50),nullable=True)
    rating:Mapped[str] = mapped_column(String(50),nullable=True)
    product_image:Mapped[str] = mapped_column(String(100))
    category_id:Mapped[int] = mapped_column(Integer,ForeignKey('category.id'))

    category:Mapped["Category"] = relationship("Category",
                                               back_populates="products")
    cart_items:Mapped[list["CartItems"]] = relationship("CartItems",
                                                  back_populates="product")