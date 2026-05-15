class Customer:
    def __init__(self,id,name,age):
        self.__id = id
        self.__name = name
        self.__age = age

    def __str__(self):
        return str(self.__id)+" : "+self.__name + " : "+str(self.__age)
    
    def __hash__(self):
        print("__hash__ called...")
        return hash(self.__id)
    
    def __eq__(self,other):
        print("__eq__ called...")
        return self.__id == other.__id

c1 = Customer(100,"A",24)
c2 = Customer(101,"B",20)
c3 = Customer(102,"C",25)
c4 = Customer(100,"D",30)
s = set()
s.add(c1)
s.add(c2)
s.add(c3)
s.add(c4)

for c in s:
    print(c)

