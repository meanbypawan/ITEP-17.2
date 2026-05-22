from threading import Thread,current_thread,Lock
import time

lock = Lock()
def transaction():
    lock.acquire()
    print(f"{current_thread().name} got Lock")
    for _ in range(5):
        print(f"{current_thread().name} executing transaction.....")
        time.sleep(4)
    lock.release()
    print(f"{current_thread().name} released the lock")

t1 = Thread(target=transaction)
t2 = Thread(target=transaction)

t1.name = "Thread T1"
t2.name = "Thread T2"

t1.start() # run() --> transaction
t2.start() # run() --> transaction