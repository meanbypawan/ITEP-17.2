from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class Department(Base):
    __tablename__ = 'department'
    serialize_rules = ("-employees.department",)
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False,unique=True)
    code:Mapped[str] = mapped_column(String(10),nullable=False,unique=True)

    employees:Mapped[list["Employee"]] = relationship("Employee",
                                                      back_populates="department",
                                                      cascade="all, delete-orphan",)

    def __repr__(self):
        return f"{self.id} {self.name} {self.code} {self.employees}"