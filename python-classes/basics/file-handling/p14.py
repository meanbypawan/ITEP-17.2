import json
# jsonpickle
p = {
    "id":100,
    "title": "Keyboard",
    "price": 500.50,
    "qty":None,
    "isWireless": True,
    "color": ("red","blue","black")
}
# json_string = json.dumps(p)
# print(p)
# print(json_string)
def write_json():
    try:
        with open("file-collection/product.json","w") as f:
            json.dump(p,f,indent=4) # json.dumps() + f.write(json_string)
            print("Operation success....")
    except Exception as e:
        print(e)

def read_json_object():
    try:
        with open("file-collection/product.json","r") as f:
            obj = json.load(f)
            print(obj)
            print(type(obj))
    except Exception as e:
        print(e)
#write_json()
read_json_object()
