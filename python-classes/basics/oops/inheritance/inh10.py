class A:
    def m1(self):
        print("A-m1()...")

class B(A):
    pass
    # def m1(self):
    #     print("B-m1()...")

class C(B):
    pass
    # def m1(self):
    #     print("C-m1()....")

print(C.mro())
print(B.mro())
print(A.mro())