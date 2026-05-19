import pickle
from Product import Product

def write_object():
  try:
   with open("file-collection/product.dat","wb") as f:
    p = Product(1,"Laptop",90000,"HP") # {id:"",title:"",price:11,"brand":""}
    pickle.dump(p,f) # {productId:1, productTitle: "",productPrice:1000}
    print("Operation success...")
  except OSError as e:
   print(e)  


def read_object():
  try: 
   with open("file-collection/product.dat","rb") as f:
     p = pickle.load(f)  
     print(p) # p.__str__()   
  except OSError as e:
    print(e)

read_object()
#write_object()