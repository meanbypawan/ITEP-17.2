# this
class Message:
    def m1(this):
        print(id(this))
        print("GM....")
    def m2(self):
        print(id(self))
        print("GN...")
    def m3():
        print("m3 executed...")    


obj = Message()

obj.m1() 
obj.m2()
Message.m3()