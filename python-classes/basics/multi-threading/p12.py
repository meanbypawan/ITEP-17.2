from threading import Thread
import time
def square(l):
    result = []
    print("Calculating square...")
    time.sleep(5)
    for element in l:
      result.append(element**2)
    print(f"Square : {result}")

def cube(l):
    result = []
    print("Calculating cube...")
    time.sleep(7)
    for element in l:
       result.append(element**3)
    print(f"Cube : {result}")

l1 = [1,2,3,4,5,6]

t1 = Thread(target=square,args=(l1,))
t2 = Thread(target=cube,args=(l1,))
t1.start()
t2.start()