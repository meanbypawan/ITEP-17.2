import pickle
from Customer import Customer
try:
    with open("file-collection/customer.dat","ab") as f:
      c = Customer(100,"ABC",9009111222,21)
      pickle.dump(c,f)
      print("Operation success....")
except OSError as e:
    print(e)