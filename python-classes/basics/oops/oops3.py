class Test:
    x = 100
    def m1(self):
      global x  
      x = 10000
      print(x)
    
    def m2(self):
        print("Inside m2()")
        print(x)

obj = Test()
obj.m1()

obj.m2()
