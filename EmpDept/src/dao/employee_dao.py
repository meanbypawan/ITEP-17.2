from sqlalchemy.exc import SQLAlchemyError
from src.db.db_config import SessionLocal
from src.model import Employee
class EmployeeDAO:
    @staticmethod
    def fetch_by_id(id):
        try:
            with SessionLocal() as session:
               emp =  session.get(Employee,id)
               if emp:
                   print(emp)
                   print(emp.department)
                   return emp
        except SQLAlchemyError as e:
            print(e)
            return None
    @staticmethod
    def save(emp:Employee):
        session = None
        try:
            with SessionLocal() as session:
                session.add(emp)
                session.commit()
                return True
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            print(e)
            return False
