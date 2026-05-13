print("At the start....")
try:
  a = int(input("Enter 1st value : ")) # ValueError
  b = int(input("Enter 2nd value : ")) # ValueError
  try:
    c = a / b
    print(f"Result : {c}")
  except ZeroDivisionError as e:
      print("Denominator can not be zero")
except ValueError as e:
  print("Only integeres are allowed...") 
       
print("At the end.......")





