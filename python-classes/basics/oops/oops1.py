# this
class Message:
    def m1(this):
        print(id(this))
        print("GM....")
    def m2(self):
        print(id(self))
        print("GN...")


obj = Message()

obj.m1() 
obj.m2()