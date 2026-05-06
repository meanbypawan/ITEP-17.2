class Test:
    message = "Hello...."  # static variable

    def __init__(self):
        print("Consturctor executed...")
        print(Test.message)
        print(self.message) # Not recommended

    def m1(self):
        print(Test.message)
        print(self.message)

    @classmethod
    def m2(cls):
        print(Test.message)
        print(cls.message)
        pass     

    @staticmethod
    def m3():
        print(Test.message)       

obj = Test()
print("After calling m1()")
obj.m1()
print("After calling m2()")
obj.m2()
print("After calling m3()")
obj.m3()
print(obj.__dict__)    
print(Test.__dict__)
print(Test.message)
print(obj.message)
