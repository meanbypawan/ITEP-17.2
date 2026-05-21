from threading import Thread,current_thread
import time
class FirstThread(Thread):
    def run(self):
        for _ in range(5):
            print(f"{current_thread().name} executing...")
            time.sleep(3)

class SecondThread(Thread):
    def run(self):
        for _ in range(5):
            print(f"{current_thread().name} executing...")
            time.sleep(1.7)

class ThirdThread(Thread):
    def run(self):
        for _ in range(5):
            print(f"{current_thread().name} executing...")
            time.sleep(0.7)


t1 = FirstThread()
t2 = SecondThread()
t3 = ThirdThread()

t1.name = "Thread-T1"
t2.name = "Thread-T2"
t3.name = "Thread-T3"

t1.start()
print(f"T1 : {t1.is_alive()}")
t1.join() # main block
print(f"T1 : {t1.is_alive()}")
print(f"{current_thread().name} resumed..")

t2.start()
t2.join() # main block
print(f"{current_thread().name} resumed..")

t3.start()
t3.join() # main block
print(f"{current_thread().name} resumed...")