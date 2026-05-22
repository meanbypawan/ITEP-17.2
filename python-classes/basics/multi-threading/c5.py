from threading import Thread, Lock, current_thread
import time
class Task:
    # class level lock
    lock = Lock()
    def __init__(self):
      pass
    def m1(self):
        with Task.lock:
            for _ in range(5):
                print(f"{current_thread().name} executing m1")
                time.sleep(1)
task1 = Task()
task2 = Task()

t1 = Thread(target=task1.m1)
t2 = Thread(target=task2.m1)

t1.name = "Thread T1"
t2.name = "Thread T2"

t1.start()
t2.start()