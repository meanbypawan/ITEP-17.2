from threading import Thread,current_thread,Lock
import time

lock = Lock()
def transaction():
   with lock:
      print(f"{current_thread().name} got lock..")
      for _ in range(5):
         print(f"{current_thread().name} executing transaction....")
         time.sleep(3)
   print(f"{current_thread().name} released the lock..")
   
t1 = Thread(target=transaction)
t2 = Thread(target=transaction)

t1.name = "Thread T1"
t2.name = "Thread T2"

t1.start() # run() --> transaction
t2.start() # run() --> transaction