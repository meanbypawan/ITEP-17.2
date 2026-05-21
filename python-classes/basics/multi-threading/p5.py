'''
  T1 ---> 5 time printing GM...
  T2 ---> 5 time printing GN...
'''
from threading import Thread
import time
class FirstThread(Thread):
    def run(self):
        for _ in range(5):
            print("GM....")
            time.sleep(1.2)

class SeconThread(Thread):
    def run(self):
        for _ in range(5):
            print("GN....")
            time.sleep(1.5)
            
t1 = FirstThread() # Ne/Born State
t2 = SeconThread() # New/Born State

t1.start() #  Runnable
t2.start() # Runnable