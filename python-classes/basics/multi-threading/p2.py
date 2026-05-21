# python3 p2.py ---> MainThread --> run
from threading import current_thread
print(current_thread().name)
print("At the end...")
print("Hello...")
print("Hi....")
print("At the start....")