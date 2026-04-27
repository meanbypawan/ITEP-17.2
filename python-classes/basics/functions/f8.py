# var-arg
def f1(a,b=100,*c):
    print(f"a : {a}")
    print(f"b : {b}")
    print(f"c : {c}")

f1(10,b = 11,21,31)    