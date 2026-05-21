from threading import Thread,current_thread
import time
class TestThread(Thread):
    def run(self):
        for _ in range(5):
            print("Test Thread executing...")
            time.sleep(1)


t1 = TestThread()
t1.start()

for _ in range(5):
    print(f"{current_thread().name} executing....")
    time.sleep(1.4)