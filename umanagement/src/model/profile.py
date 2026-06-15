from sqlalchemy import Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db_config import Base


class Profile(Base):
    __tablename__ = 'profile'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    father_name:Mapped[str] = mapped_column(String(100),nullable=False)
    dob:Mapped[Date] = mapped_column(Date)
    email:Mapped[str] = mapped_column(String(100),nullable=False,unique=True)
    contact:Mapped[str] = mapped_column(String(10),nullable=False)
    student_id:Mapped[int] = mapped_column(ForeignKey('student.id'),nullable=False,unique=True)



