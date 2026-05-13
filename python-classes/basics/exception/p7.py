# try --> all except --> finally
print("At the start....")

try:
  a = int(input("Enter 1st value : ")) # ValueError
  b = int(input("Enter 2nd value : ")) # ValueError
  c = a / b # ZeroDivisonError
  print(f"Result : {c}")

except (ZeroDivisionError,ValueError) as e:
  print("Oops! something went wrong...")

print("At the end.......")





