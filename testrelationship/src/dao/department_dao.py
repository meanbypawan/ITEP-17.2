from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.db.db_config import SessionLocal
from src.model import Employee
from src.model.department import Department
class DepartmentDAO:
    @staticmethod
    def fetch_all():
        try:
          with SessionLocal() as session:
              # select * from Department
              stmt = select(Department)
              result = session.execute(stmt).scalars().all()
              for department in result:
                  print(department.to_dict())

        except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def save_employees_in_department(dept_id):
        session = None
        try:
            with SessionLocal() as session:
                dept = session.get(Department,dept_id)
                if dept:
                       dept.employees.append(Employee(name="Sauraf",salary="99000",skill="PowerBI"))
                       dept.employees.append(Employee(name="Ganesh",salary="91000",skill="Excel"))
                       #session.add(dept)
                       session.commit()
                       return True
                else:
                    return False
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            print(e)
            return False
    @staticmethod
    def save(dept:Department):
        session = None
        try:
            with SessionLocal() as session:
                session.add(dept) # Pending :[Attached with session]
                session.commit() # Persistant
                return True
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            print(e)
            return False



