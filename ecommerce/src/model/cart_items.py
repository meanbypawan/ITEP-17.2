from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class CartItems(Base):
    __tablename__ = "cart_items"
    cart_id:Mapped[int] = mapped_column(Integer,
                                        ForeignKey("cart.id"),
                                        primary_key=True,)
    product_id:Mapped[int] = mapped_column(Integer,
                                           ForeignKey("product.id"),
                                           primary_key=True)
    cart:Mapped["Cart"] = relationship("Cart",
                                       back_populates="cart_items",
                                       lazy="selectin")

    product:Mapped["Product"] = relationship("Product",
                                             back_populates="cart_items",
                                             lazy="selectin")