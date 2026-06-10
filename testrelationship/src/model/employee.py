from sqlalchemy import Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class Employee(Base):
    __tablename__ = 'employee'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    salary:Mapped[float] = mapped_column(Numeric(10,2),nullable=False)
    skill:Mapped[str] = mapped_column(String(1000))
    department_id:Mapped[int] = mapped_column(ForeignKey('department.id'))

    department:Mapped["Department"] = relationship("Department",
                                                   back_populates="employees")

    def __repr__(self):
        return f"{self.id} {self.name} {self.salary} {self.skill} {self.department_id}"