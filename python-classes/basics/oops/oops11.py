class Test:
    x = 100
    def __init__(self,x):
        print(self.x)
        print(x)

    def m1(self):
        print("Inside m1()")
        print(self.x) # :- 500 
        print(Test.x) # :- 100

obj = Test(200)
obj.x = 500
obj.m1()
print(obj.__dict__)