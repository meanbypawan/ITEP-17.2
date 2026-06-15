from src.dao.course_dao import CourseDAO
from src.dao.department_dao import DepartmentDAO
from src.model import Department


def save_department():
    name = input("Enter department name: ")
    dept = Department(departement_name=name)
    if DepartmentDAO.save(dept):
        print("Department saved...")
    else:
        print("Department not saved...")

def fetch_all_departments():
    departments = DepartmentDAO.fetch_all()
    print(departments)
#fetch_all_departments()

CourseDAO.fetch_all()

#save_department()
