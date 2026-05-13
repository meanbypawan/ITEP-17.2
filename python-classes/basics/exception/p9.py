'''
1. Can we write multiple except block corresponding to single try:
ans:- yes but order must be child to parent [Top-Bottom]. Parent
except block must be placed at the last.

'''
import math

print("At the start...")
try:
  a = int(input("Enter 1st value : ")) # ValueError
  b = int(input("Enter 2nd value : ")) # ValueError
  c = a / b # ZeroDivisionError
  math.exp(1000) # OverflowError
  # Statement --- 15
except ArithmeticError as e:
    print(f"AritmeticError : {e}")
            
except Exception as e:
  print(f"Error : {e}")    


print("At the end....")
