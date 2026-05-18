import pickle
class Employee:
    def __init__(self,id,name,salary,age):
        self.__id = id
        self.__name = name
        self.__salary = salary
        self.__age = age
    def __str__(self):
        print(f"Id :{self.__id}\nName : {self.__name}\nAge : {self.__age}\nSalary : {self.__salary}")
        return ""

# python3 p7.py
#print(f"__name__ : {__name__}") # "__main__"

if __name__ == "__main__":
    try:
        with open("file-collection/employee.dat","ab") as f:
            emp = Employee(102,"Cheeku",950000,21)
            pickle.dump(emp,f) # Serialization
            print("Operation success....")
    except OSError as e:
        print(e)