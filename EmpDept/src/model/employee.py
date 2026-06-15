
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.db.db_config import Base


class Employee(Base):
    __tablename__ = 'employee'
    id = mapped_column(Integer,primary_key=True)
    name = mapped_column(String(100))
    salary = mapped_column(Integer)
    skill = mapped_column(String(100))
    department_id = mapped_column(ForeignKey('department.id'))
    department:Mapped["Department"] = relationship("Department")

    def __repr__(self):
        return f"id={self.id} name={self.name} salary={self.salary} skill={self.skill}"
    