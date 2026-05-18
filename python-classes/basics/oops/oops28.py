class Employee:
    
    def __init__(self,id,name,salary):
        self.__id = id
        self.__name = name
        self.__salary = salary
    
    def __hash__(self):
        return hash(self.__id)
    
    def __eq__(self,other):
        return self.__id == other.__id and self.__name == other.__name
    
    def __str__(self):
        return str(self.__id)+" : "+self.__name+" : "+str(self.__salary)

s = set()
e1 = Employee(100,"A",90000)
e2 = Employee(101,"B",120000)
e3 = Employee(101,"C",150000)
e4 = Employee(100,"A",90000)

s.add(e1)
s.add(e2)
s.add(e3)
s.add(e4)

for e in s:
    print(e)