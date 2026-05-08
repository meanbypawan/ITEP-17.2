'''
1. Employee Management System
Problem

Create an Employee class to manage employee details.

Requirements

Each employee should have:

employee id
name
department
salary
Functionalities
Display employee details
Increase salary by percentage
Count total employees created using a class variable

Create employee object from a string:

"101-Atul-IT-50000"

Employee 
  Property- (id,name,department,salary)
  Behaviour :- display(self),increase_salary(self,percentage)

__new__ :- create the object in python  

__ [private]
_ [protect]

'''
class Employee:
    __counter = 0
    def __init__(self,id,name,department,salary):
        self.__id = id
        self.__name = name
        self.__department = department
        self.__salary = int(salary)
        Employee.__counter += 1
        
    def display(self):
        print(f"Id : {self.__id}\nName : {self.__name}\nDepartment : {self.__department}\nSalary : {self.__salary}")

    def increment_salary(self,per):
        self.__salary += (self.__salary*per)/100

    @classmethod    
    def from_string(cls,emp_data):
        id,name,department,salary = emp_data.split("-")
        return cls(id,name,department,salary) # it will invoke constructor
    @classmethod
    def total_employee(cls):
        return Employee.__counter

e1 = Employee.from_string("101-Atul-IT-50000")
e1.display()
