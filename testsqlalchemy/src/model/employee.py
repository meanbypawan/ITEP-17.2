from sqlalchemy import Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db_config import Base

class Employee(Base):
    __tablename__ = 'employee'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    salary:Mapped[float] = mapped_column(Numeric(10,2),nullable=False)
    department:Mapped[str] = mapped_column(String(100),nullable=False)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.id)+":"+self.name+":"+str(self.salary)+":"+self.department