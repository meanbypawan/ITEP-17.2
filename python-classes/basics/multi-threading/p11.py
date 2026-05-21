from threading import Thread,current_thread
import time

def say_something(message):
    for _ in range(5):
        print(f"{message}....{current_thread().name}")
        time.sleep(1)

t1 = Thread(target=say_something,args=("Hello",))
t2 = Thread(target=say_something,args=("Welcome",))

t1.name = "Thread-T1"
t2.name = "Thread-T2"
t1.start()        
t2.start()