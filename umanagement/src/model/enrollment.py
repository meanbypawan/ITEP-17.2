from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class Enrollment(Base):
    __tablename__ = 'enrollment'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    student_id:Mapped[int] = mapped_column(ForeignKey('student.id'))
    course_id:Mapped[int] = mapped_column(ForeignKey('course.id'))

    student:Mapped["Student"] = relationship("Student")
    course:Mapped["Course"] = relationship("Course")