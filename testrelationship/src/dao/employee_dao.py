from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from src.model.employee import Employee
from src.db.db_config import SessionLocal


class EmployeeDAO:
    @staticmethod
    def fetch_by_skill(skill):
        try:
            with SessionLocal() as session:
                # seleect * from employee where skill = %s
                stmt = select(Employee).where(Employee.skill == skill)
                result = session.execute(stmt).scalars().all()
                result = [emp.to_dict() for emp in result]
                print(result)
        except SQLAlchemyError as e:
            print(e)
    @staticmethod
    def fetch_all():
        try:
            with SessionLocal() as session:
                stmt = select(Employee)
                result = session.execute(stmt).scalars().all()
                result = [emp.to_dict() for emp in result]
                print(result)
        except SQLAlchemyError as e:
            print(e)