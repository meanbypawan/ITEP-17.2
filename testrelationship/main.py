from src.dao.department_dao import DepartmentDAO
from src.dao.employee_dao import EmployeeDAO
from src.model import Department


def save_department():
    name = input("Enter department name: ")
    code = input("Enter department code: ")

    dept = Department(name=name, code=code)
    print(DepartmentDAO.save(dept))


#save_department()
#print(DepartmentDAO.save_employees_in_department(1))
#print(DepartmentDAO.fetch_all())
#EmployeeDAO.fetch_all()
EmployeeDAO.fetch_by_skill("PowerBI")