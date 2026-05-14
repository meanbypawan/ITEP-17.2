print("At the start...")
f = None
try:
 f = open("python_introduction.txt","r") 

except FileNotFoundError as e:
 print("Except Block Executed...")
 print("File not available...")

else:
  print("Else block executed....")
  data = f.read()
  print(data)

finally:
 print("Finally Block executed...")
 if f is not None:
  f.close()

print("At the end...")