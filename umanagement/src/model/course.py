from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class Course(Base):
    __tablename__ = 'course'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    course_code:Mapped[str] = mapped_column(String(10),unique=True,nullable=False)
    course_name:Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    department_id:Mapped[int] = mapped_column(ForeignKey('department.id'))
    department:Mapped["Department"] = relationship("Department")

    enrollments:Mapped[list["Enrollment"]] = relationship("Enrollment")

    def __repr__(self):
        return f"Course = {self.course_code} : {self.course_name}"