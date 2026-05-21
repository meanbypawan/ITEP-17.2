'''
  T1 ---> 5 time printing GM...
  T2 ---> 5 time printing GN...
'''
from threading import Thread
class FirstThread(Thread):
    def run(self):
        for _ in range(5):
            print("GM....")

class SeconThread(Thread):
    def run(self):
        for _ in range(5):
            print("GN....")

t1 = FirstThread() # Ne/Born State
t2 = SeconThread() # New/Born State

t1.start() #  Runnable
t2.start() # Runnable