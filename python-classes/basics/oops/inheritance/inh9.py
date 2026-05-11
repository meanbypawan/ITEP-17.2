class A:

    def __init__(self):
        print("A class constructor.....")

    def m1(self):
        print("A-m1()...")
    
    @classmethod
    def m2(cls):
      print("A-m2() class method....")
    
    @staticmethod
    def m3():
        print("A-m3() static method....")

class B(A):
  def __init__(self):
    print("B class constructor...")
    super().__init__()
    super().m1()
    super().m2()
    super().m3()

  def x(self):
    print("Child class x method...")
    super().m1()
    super().m2()
    super().m3()

  @classmethod
  def y(cls):
    print("Chlild class class method called...")
    #super().m1()
    super().m2()
    super().m3()
    pass
  
  @staticmethod
  def z():
    #super().m1()
    super().m3()
obj = B()
print("Calling child class instance method....")  
obj.x()
print("Calling child class class method................")
obj.y()
print("Calling child class static method...")
obj.z()