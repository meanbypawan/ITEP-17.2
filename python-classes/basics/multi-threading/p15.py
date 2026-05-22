from threading import Thread,current_thread,Lock
# race condition
# LEGB :-  Local-->Enclosing--->Global---->Builtins
lock = Lock()
counter = 0
def increment():
  global counter
  with lock:
   for _ in range(1000000):
      counter = counter + 1


t1 = Thread(target=increment)
t2 = Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)

