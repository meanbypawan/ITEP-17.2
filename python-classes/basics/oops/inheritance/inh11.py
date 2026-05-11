class A:
    def m1(self):
        print("A-m()...")

class B:
    def m1(self):
        print("B-m1()....")

class C(A,B):
    def m1(self):
        print("C-m1()...")
        super().m1()

obj = C()
obj.m1() 