from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.db.db_config import SessionLocal
from src.model import Course, Department
from src.model.course import Course

class CourseDAO:
    def fetch_all():
        try:
            with SessionLocal() as session:
                statement = select(Course)
                result = session.execute(statement).scalars().all()
                for course in result:
                    #print(f"{course.course_code} {course.course_name} Department Name : {course.department.departement_name}")
                    print(course)
        except SQLAlchemyError as e:
            print(e)
            return None