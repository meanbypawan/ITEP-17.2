# Abstract class and Abstract method

from abc import abstractmethod,ABC

class A(ABC):
    def __init__(self):
        print("Abstract class instantiated....")
    
    

obj = A()