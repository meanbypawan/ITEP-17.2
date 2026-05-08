import time
import gc
class Test:
    
    def __init__(self):
        print("Object created...")
    

    def __del__(self):
        print("Obect desctroyed.....")


print(gc.isenabled())
print(gc.disable())
print(f"After Disable : {gc.isenabled()}")


