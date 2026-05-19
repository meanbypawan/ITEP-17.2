import json
p = {
    "id":100,
    "title": "Keyboard",
    "price": 500.50,
    "qty":None,
    "isWireless": True
}

# PO --> JsonString
json_string = json.dumps(p) # dump  v/s dumps
print(f"Python Object : {p}")
print(f"Json String {json_string}") 

# Json_string --> PO
obj = json.loads(json_string) # load v/s loads
print(f"Python Object : {obj}")