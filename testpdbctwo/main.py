from dao.employee_dao import EmployeeDAO
from model.employee import Employee
while True:
    print("Press 1 for insertion")
    print("Press 2 for fetchall")
    print("Press 3 for update")
    print("Press 4 for delete")
    print("Press 5 fro fetch by id")
    print("Press 0 for exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        salary = float(input("Enter your salary: "))
        department = input("Enter your department: ")
        emp = Employee(None,name,salary,department)
        if EmployeeDAO.save(emp):
            print("Employee saved")
        else:
            print("Something went wrong")
    elif choice == 0:
        break
    elif choice == 2:
        EmployeeDAO.fetch_all()
    elif choice == 3:
        name = input("Enter your name: ")
        salary = float(input("Enter your salary: "))
        department = input("Enter your department: ")
        id = int(input("Enter employee id: "))
        emp = Employee(id,name,salary,department)
        if EmployeeDAO.update(emp) :
            print("Record updated successfully")
        else:
            print("Something wrong...")
    elif choice == 4:
        id = int(input("Enter employee id : "))
        if EmployeeDAO.delete(id) :
            print("Record delted...")
        else :
            print("Something wrong....")
    elif choice == 5:
        id = int(input("Enter employee id : "))
        EmployeeDAO.find_by_id(id)