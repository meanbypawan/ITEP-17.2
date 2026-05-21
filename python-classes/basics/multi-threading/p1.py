# By using function
# By extending Thread class

from threading import Thread
#Thread, FirstThread
class FirstThread(Thread):
    def run(self):
        print("Run executed....")
        

# FirstThread IS-A Thread
t1 = FirstThread()
t2 = FirstThread()
t1.start() #start() ---> run()
t2.start()