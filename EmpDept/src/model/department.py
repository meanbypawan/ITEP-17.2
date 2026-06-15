from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.db.db_config import Base


class Department(Base):
    __tablename__ = 'department'
    id = mapped_column(Integer,primary_key=True)
    name = mapped_column(String(100),unique=True)
    code = mapped_column(String(100),unique=True)
    employees:Mapped[list["Employee"]] = relationship("Employee",
                                                      cascade="all, delete-orphan",)

    def __repr__(self):
        return f"id = {self.id} name = {self.name} code = {self.code}"