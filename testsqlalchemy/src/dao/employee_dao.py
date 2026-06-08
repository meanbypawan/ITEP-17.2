from sqlalchemy.exc import SQLAlchemyError

from src.db.db_config import SessionLocal
from src.model.employee import Employee


class EmployeeDAO:
    @staticmethod
    def fetch_by_id(emp_id):
        try:
            with SessionLocal() as session:
               emp =  session.get(Employee,emp_id)
               return emp
        except SQLAlchemyError as e:
            print(e)
            return None

    @staticmethod
    def update_by_id(emp:Employee):
        session = None
        try:
            with SessionLocal() as session:
                db_emp = session.get(Employee,emp.id)
                if db_emp:
                    db_emp.name = emp.name
                    db_emp.salary = emp.salary
                    db_emp.department = emp.department
                    session.commit()
                    return True
                else:
                    return False
        except SQLAlchemyError as e:
            print(e)
            return False
    @staticmethod
    def delete(id):
        session = None
        try:
            with SessionLocal() as session:
               emp =  session.get(Employee,id)
               if emp:
                   session.delete(emp)
                   session.commit()
                   return "Resource successfully deleted"
               else:
                   return "Requested Resource not found"

        except SQLAlchemyError as e:
            if session:
                session.rollback()
            print(e)
            return "Something went wrong"
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