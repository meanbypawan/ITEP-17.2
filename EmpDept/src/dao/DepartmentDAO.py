from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.db.db_config import SessionLocal
from src.model import Department
class DepartmentDAO:
    @staticmethod
    def fetch_all():
        try:
            with SessionLocal() as session:
                statement = select(Department)
                result = session.execute(statement).scalars().all()
                return result
        except SQLAlchemyError as e:
            print(e)
            return None
    @staticmethod
    def save(department:Department):
        session = None
        try:
            with SessionLocal() as session:
                session.add(department)
                session.commit()
                return True
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            print(e)
            return False