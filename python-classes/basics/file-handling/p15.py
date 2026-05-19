import requests
import json
response = requests.get("https://dummyjson.com/products")

json_response = response.json()

print(json_response)

def write_api_response(data):
  try:
     with open("file-collection/product.json","w") as f:
        json.dump(data,f,indent=4)
        print("Operation success...")
  except Exception as e:
     print(e)
 
#write_api_response(json_response) 
def read_file():
   try:
      with open("file-collection/product.json") as f:
        data =  json.load(f)
        product_list = data["products"]
        for product in product_list:
           print(product["title"]," : ",product["price"])
   except Exception as e:
      print(e)

read_file()      