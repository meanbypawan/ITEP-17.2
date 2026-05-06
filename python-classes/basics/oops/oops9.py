'''
  class Test{
    int a;
    int b;
    int c;
  }
  new Test()
'''
class Test:
    def __init__(self):
        self.a = 100

    def m1(self):
        self.b = 200
    
    @classmethod
    def m2(cls):
        pass     

obj = Test()

print(obj.__dict__)

obj.m1()

print(obj.__dict__)

obj.c = 300

print(obj.__dict__) 