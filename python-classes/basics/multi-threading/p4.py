from threading import Thread,current_thread
class FirstThread(Thread):
    def run(self):
        for _ in range(5):
            print(f"Hello....{current_thread().name}")


t1 = FirstThread()
t2 = FirstThread()

#t1.setName("Thread-T1")
#t2.setName("Thread-T2")
t1.name = "Thread-T1"
t2.name = "Thread-T2"

t1.start()
t2.start()