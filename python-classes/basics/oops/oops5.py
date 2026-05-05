'''
   AithmeticOperation
     a,b
     add(), sub(), mult(), div
'''

class AirthmeticOperation:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def add(self):
       return self.__a + self.__b

    def multiplication(self):       
       return self.__a * self.__b  

obj = AirthmeticOperation(20,10)
print(f"Addition : {obj.add()}")
print(f"Multiplication : {obj.multiplication()}")