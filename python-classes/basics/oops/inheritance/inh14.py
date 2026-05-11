# Abstract class and Abstract method

from abc import abstractmethod
class A:
    def __init__(self):
        print("Abstract class instantiated....")
        
    @abstractmethod
    def m1(self):
      pass
    

obj = A()