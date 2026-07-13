from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class Cart(Base):
    __tablename__ = 'cart'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    user_id:Mapped[int] = mapped_column(Integer,ForeignKey("user.id"),
                                        unique=True)
    user:Mapped["User"] = relationship("User",
                                       back_populates="cart")

    cart_items:Mapped[list["CartItems"]] = relationship("CartItems",
                                                  back_populates="cart",
                                                  cascade="all, delete-orphan")