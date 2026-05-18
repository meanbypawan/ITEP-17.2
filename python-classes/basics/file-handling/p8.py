import pickle
from p7 import Employee
try:
    with open("file-collection/employee.dat","rb") as f:
        emp = pickle.load(f) # Deserialization/Unpickling.
        print(emp)
        emp = pickle.load(f)
        print(emp)
except OSError as e:
    print(e)