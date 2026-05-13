import math

print("At the start...")
try:
  a = int(input("Enter 1st value : ")) # ValueError
  b = int(input("Enter 2nd value : ")) # ValueError
  c = a / b # ZeroDivisionError
  math.exp(1000) # OverflowError
except ArithmeticError as e:
    print(f"AritmeticError : {e}")        
print("At the end....")
