# seek(), tell()
f = None
try:
   f = open("file-collection/abc.txt","r")
   # data = f.read()
   for line in f:
      print(line)
except OSError as e:
   print(e)
finally:
   if f is not None:
      f.close()   