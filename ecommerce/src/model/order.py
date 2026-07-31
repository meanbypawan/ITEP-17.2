import datetime
from datetime import datetime

from sqlalchemy import Integer, ForeignKey, Numeric, String, DateTime, Date, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class Order(Base):
    __tablename__ = "orders"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    user_id:Mapped[int] = mapped_column(Integer,ForeignKey("user.id"))
    totalBillAmount:Mapped[float] = mapped_column(Numeric(10,2))
    name:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(100))
    contact:Mapped[str] = mapped_column(String(10))
    address:Mapped[str] = mapped_column(String(255))
    date:Mapped[datetime] = mapped_column(DateTime,default=datetime.now)
    payment_mode:Mapped[str] = mapped_column(String(10),default="COD")

    order_items:Mapped[list["OrderItems"]] = relationship("OrderItems",
                                                          back_populates="order",
                                                          cascade="all, delete-orphan")
