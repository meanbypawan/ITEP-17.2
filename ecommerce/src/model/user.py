from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class User(Base):
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(100),unique=True)
    password:Mapped[str] = mapped_column(String(70))
    contact:Mapped[str] = mapped_column(String(10),unique=True)

    cart:Mapped["Cart"] = relationship("Cart",
                                       back_populates="user",
                                       cascade="all, delete-orphan",
                                       uselist=False)