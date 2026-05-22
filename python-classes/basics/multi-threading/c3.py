from threading import Thread, Lock, current_thread
import time
class Task:
    def __init__(self):
        self.lock = Lock()
    def m1(self):
        with self.lock:
            for _ in range(5):
                print(f"{current_thread().name} executing m1")
                time.sleep(1)
    
    def m2(self):
        with self.lock:
            for _ in range(5):
                print(f"{current_thread().name} executing m2")
                time.sleep(1)
    
    def m3(self):
            for _ in range(5):
                print(f"{current_thread().name} executing m3")
                time.sleep(3)                        
task = Task()

t1 = Thread(target=task.m1)
t2 = Thread(target=task.m2)
t3 = Thread(target=task.m3)

t1.name = "Thread T1"
t2.name = "Thread T2"
t3.name = "Thread T3"

t1.start()
t2.start()
t3.start()