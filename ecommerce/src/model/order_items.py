from sqlalchemy import Integer, ForeignKey, String, Numeric
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from src.db.db_config import Base


class OrderItems(Base):
    __tablename__ = "order_items"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    order_id:Mapped[int] = mapped_column(Integer,ForeignKey("orders.id"))
    title:Mapped[str] = mapped_column(String(100))
    price:Mapped[float] = mapped_column(Numeric(10,2))
    description:Mapped[str] = mapped_column(String(255))
    qty:Mapped[int] = mapped_column(Integer)
    totalPrice:Mapped[float] = mapped_column(Numeric(10,2))
    product_image:Mapped[str] = mapped_column(String(100))
    warranty_information:Mapped[str] = mapped_column(String(50),nullable=True)
    product_id:Mapped[int] = mapped_column(Integer)
    order:Mapped["Order"] = relationship("Order",
                                         back_populates="order_items")