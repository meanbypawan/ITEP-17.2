# Abstract class and Abstract method

from abc import abstractmethod,ABC

class A(ABC):
    def __init__(self):
        print("Abstract class instantiated....")
    
    @abstractmethod 
    def wish(self):
        pass

    def say_hello(self):
        print("Hell....")

class AImpl(A):
    def wish(self):
        print("GM......")

obj = AImpl()    
obj.wish()
obj.say_hello()