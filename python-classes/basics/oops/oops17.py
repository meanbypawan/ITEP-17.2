class Laptop:
    def __init__(self,price):
        self.__price = price

    def __add__(self,other):
     temp = Laptop(None)
     temp.__price = self.__price + other.__price   
     return temp
    
    def __str__(self):
        return str(self.__price)

l1 = Laptop(50000)
l2 = Laptop(75000)
l3 = Laptop(55000)
print(l1 + l2 + l3)