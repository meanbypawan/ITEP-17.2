import pickle
from p7 import Employee
try:
    with open("file-collection/employee.dat","rb") as f:
      while True:
         try:
           emp = pickle.load(f)
           print(emp)
         except EOFError as e:
            break
except OSError as e:
    print(e)