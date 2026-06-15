from src.dao.DepartmentDAO import DepartmentDAO
from src.dao.employee_dao import EmployeeDAO
from src.model import Department, Employee

# d1 = Department(name="HR",code="IF-HR")
# d2 = Department(name="IT",code="IF-IT")
#
# print(DepartmentDAO.save(d1))
# print(DepartmentDAO.save(d2))
# result = DepartmentDAO.fetch_all()
# for department in result:
#     print(department)

# e1 = Employee(name="D",skill="Python",salary=5000,department_id=2)
# print(EmployeeDAO.save(e1))

emp = EmployeeDAO.fetch_by_id(1)
