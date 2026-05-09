'''
  super() :- it is used to call parent class member from child class.
'''
class Parent:
    def __init__(self):
        print("Parent init called...")

    def m1(self):
        print("parent--m1")

class Child(Parent):
    def __init__(self):
        print("Child init called...")

    def m1(self):
        super().m1()
        print("child-m1")    

obj = Child()
obj.m1()