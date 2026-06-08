from src.db.db_config import Base
from src.db.db_config import engine
from src.model.employee import Employee
from src.dao.employee_dao import EmployeeDAO
Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)
while True:
    print("Press 1 for insertion....")
    print("Press 2 for deletion....")
    print("Press 3 for fetch by id....")
    print("Press 4 for update by id....")
    print("Press 0 for exit...")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        salary = float(input("Enter your salary: "))
        department = input("Enter your department: ")
        emp = Employee(name=name, salary=salary, department=department)
        if EmployeeDAO.save(emp):
            print("Employee saved")
        else:
            print("Something went wrong")
    elif choice == 0:
        break
    elif choice == 2:
        id = int(input("Enter employee id: "))
        result = EmployeeDAO.delete(id)
        print(result)
    elif choice == 3:
        id = int(input("Enter employee id: "))
        emp = EmployeeDAO.fetch_by_id(id)
        if emp:
            print(emp)
        else:
            print("Something went wrong")
    elif choice == 4:
      id = int(input("Enter employee id: "))
      emp = EmployeeDAO.fetch_by_id(id)
      if emp:
          print(emp)
          name = input("Enter your name: ")
          salary = float(input("Enter your salary: "))
          department = input("Enter your department: ")
          emp = Employee(name=name, salary=salary, department=department,id=id)
          if EmployeeDAO.update_by_id(emp):
              print("Employee updated")
          else:
              print("Something went wrong")
      else:
          print("Resource not found..")





