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
t1.join(timeout=10) # Main Block

t2.start()
t3.start()

for _ in range(5):
    print(f"{current_thread().name} is executing")
    time.sleep(5)