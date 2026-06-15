from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class Student(Base):
    __tablename__ = 'student'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    rollnumber:Mapped[str] = mapped_column(String(20),nullable=False,unique=True,index=True)

    profile:Mapped["Profile"] = relationship("Profile",
                                             cascade="all,delete-orphan")

    enrollments:Mapped[list["Enrollment"]] = relationship("Enrollment")








