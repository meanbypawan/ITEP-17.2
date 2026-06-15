from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base
class Department(Base):
    __tablename__ = 'department'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    departement_name:Mapped[str] = mapped_column(String(100),unique=True,nullable=False)

    courses:Mapped[list["Course"]] = relationship("Course",
                                                  cascade="all,delete-orphan")

    def __repr__(self):
        return f"{self.id} : {self.departement_name}"