from threading import Thread,current_thread,Lock
import time
class Task:
    def __init__(self):
        self.lock = Lock()

    def transaction(self):
        with self.lock:
          for _ in range(5):
            print(f"{current_thread().name} Executing transaction....") 
            time.sleep(2)

task  = Task()

t1 = Thread(target=task.transaction)
t2 = Thread(target=task.transaction)
t1.name = "Thread T1"
t2.name = "Thread T2"

t1.start()
t2.start()