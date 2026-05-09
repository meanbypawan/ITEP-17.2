class Parent:
    def __init__(self):
        print("Parent init called...")
class Child(Parent):
    def __init__(self):
        super().__init__(self)
        print("Child init called....")

obj = Child()        