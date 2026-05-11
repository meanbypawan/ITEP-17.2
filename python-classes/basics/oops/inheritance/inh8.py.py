# super() -: it is ued to call parent class member from child class
class A:
    def wish(self):
        print("GM....")

    def say_hello(self):
       print("Hello....")

class B(A):
    def wish(self):
        super().wish()
        print("GN.....")

obj = B()
obj.wish()
obj.say_hello()    
