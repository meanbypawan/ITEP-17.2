class Customer:
    def __init__(self):
        self.id = 100
    
    def set_name(self,name):
        self.name = name
    
    def display_contact(self):
        print(f"Contact : {self.contact}")

print(Customer.__dict__)
obj = Customer()
print(obj.__dict__)

obj.set_name("Atul")
print(obj.__dict__)

obj.contact = 9009111222
print(obj.__dict__) 
obj.display_contact()   