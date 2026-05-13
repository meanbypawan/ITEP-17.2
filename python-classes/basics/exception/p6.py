# try --> all except --> finally
print("At the start....")

try:
  a = int(input("Enter 1st value : ")) # ValueError
  b = int(input("Enter 2nd value : ")) # ValueError
  c = a / b # ZeroDivisonError
  print(f"Result : {c}")

except ZeroDivisionError as e:
  print("Denominator can not be zero..")

except ValueError as e:
  print("Only integers are allowed...")

finally:
    print("Finally block executed......")

print("At the end.......")





