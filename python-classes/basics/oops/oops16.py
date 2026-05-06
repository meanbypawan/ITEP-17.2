'''
  Distance :- [km,meter]
'''
class Distance:
    def __init__(self,km,meter):
        self.__km = km
        self.__meter = meter
    
    def display(self):
        print(f"{self.__km} km {self.__meter} meter")

    def __add__(self,other):
        temp = Distance(0,0)
        temp.__km = self.__km + other.__km
        temp.__meter = self.__meter + other.__meter
        if temp.__meter >= 1000:
            temp.__km += 1
            temp.__meter -= 1000
        return temp    

d1 = Distance(5,700)
d2 = Distance(2,500)
d1.display()
d2.display()

d3 = d1 + d2

d3.display()
       