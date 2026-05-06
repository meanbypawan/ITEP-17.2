'''
  self refer current object in class
  When we call method by object, PVM pass current object as a argument.
'''
class Test:

    def m1(self): # self :- reference of current object
        print("m1()-executed.....")

    @classmethod
    def m2(cls): # cls :- reference of current class
        print("m2()-executed../ class method")

    @staticmethod
    def m3(): # it is only for the utility purpose
        print("m3()-executed../ static method")

    def m4():
        print("m4-executed...")

obj = Test()
obj.m1()
obj.m2()
obj.m3()
obj.m4() #