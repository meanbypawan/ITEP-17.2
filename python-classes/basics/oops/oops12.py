x = 5000
class Test:
    x = 100
    y = 200

    def m1(self):
      print(x)

obj1 = Test()
obj1.x = 1000

obj2 = Test()
obj2.y = 2000

print(obj1.x,"  ",obj1.y) # 1000 200
print(obj2.x,"  ",obj2.y) # 100 2000

