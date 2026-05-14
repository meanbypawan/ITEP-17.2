import os
import sys
print("At the start.....")
try:
    #os._exit(0) 
    sys.exit(0)
    a = int(input("Enter 1st value : "))
    b = int(input("Enter 2nd value : "))
    c = a / b
    print(f"Result : {c}")

except Exception as e:
    print("Excption caught") 

finally:
  print("Finally executed....")       

print("At the end...")