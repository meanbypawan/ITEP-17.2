f = None
try:
  f = open("file-collection/abc.txt","r")  # OSError,FileNotFoundError,PermissionError
  # Read or write operation
  data = f.read()
  #data = f.read(6)
  #data = f.readline()
  #data = f.readlines()
  print(data)
except OSError as e:
  print(e)

finally:
  if f is not None:
    f.close()  