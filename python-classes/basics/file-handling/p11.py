import pickle
from Customer import Customer
try:
    with open("file-collection/customer.dat","rb") as f:
        c = pickle.load(f)
        print(c)
except OSError as e:
    print(e)