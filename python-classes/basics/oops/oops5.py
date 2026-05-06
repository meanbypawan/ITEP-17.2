'''
  Nested Class :-

'''
class AITR:
  class MCADepartment:
    pass

  class BEDepartment:
    pass  

class Person:
  class DOB:
    def __init__(self,dd,mm,yy):
      self.dd = dd
      self.mm = mm
      self.yy = yy

  def __init__(self,name,dd,mm,yy):
        self.__name = name
        self.__dob = self.DOB(dd,mm,yy)

  def display(self):
    print(f"Name : {self.__name}")
    print(f"DOB {self.__dob.dd}/{self.__dob.mm}/{self.__dob.yy}")

         

p = Person("Atul",2,10,1990)
p.display()