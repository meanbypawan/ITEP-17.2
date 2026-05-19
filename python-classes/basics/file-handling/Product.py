class Product:
    def __init__(self,id,title,price,brand):
        self.id = id
        self.title = title
        self.price = price
        self.brand = brand

    def __str__(self):
        return str(self.id)+":"+self.title+":"+str(self.price)+":"+self.brand    

    # during serialization process - dump()
    def __getstate__(self):
        print("__getstate__ called...")
        return {
            "productId": self.id,
            "productTitle": self.title,
            "productPrice": self.price
        }
    # during deserialization process - load()  
    def __setstate__(self,state):
        print(state)
        self.id = state["productId"]
        self.title = state["productTitle"]
        self.price = state["productPrice"]
        self.brand = ""
