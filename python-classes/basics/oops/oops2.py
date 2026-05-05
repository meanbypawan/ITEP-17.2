'''
  Customer [id,name,contact,accountNo]
  view_info()


'''
class Customer:
    def __init__(self):
      self.id = 100
      self.name = "Atul"
      self.contact = 9009111222
      self.account_no = "at00013333"
      


obj = Customer() # obj {id: 100, name: "Atul", contact: 9009111222, ac:"at3434"}
print(f"Id : {obj.id}")
print(f"Name : {obj.name}")
print(f"Contact : {obj.contact}")
print(f"Account : {obj.account_no}")
