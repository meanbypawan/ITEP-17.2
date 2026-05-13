'''
  Printing exception related information :-
  1. type of exeception
  2. get exception class name
  3. exception name
'''
print("At the start....")
a = int(input("Enter 1st value : ")) # ValueError
b = int(input("Enter 2nd value : ")) # ValueError
try:
  c = a / b
  print(f"Result : {c}")
except ZeroDivisionError as e:
    print("Denominator can not be zero")
    # print(f"Type of exception : {type(e)}") 
    # print(f"Exception class : {e.__class__}")
    # print(f"Exception : {e.__class__.__name__}")
    # print(f"Printin Exception Object : {e}") 
print("At the end.......")





