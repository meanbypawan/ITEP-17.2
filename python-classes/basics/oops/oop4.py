class Customer:
    def __init__(self,id,name,contact,account_no):
        self.id = id
        self.name = name
        self.contact = contact
        self.account_no = account_no

    def display(self):
        print(f"Id : {self.id}")
        print(f"Name : {self.name}")
        print(f"Cotnact : {self.contact}")
        print(f"Account No : {self.account_no}")

id = int(input("Enter customer id : "))
name = input("Enter customer name : ")
contact = int(input("Enter contact number : "))
account_no = input("Enter account no : ")

c1 = Customer(id,name,contact,account_no)
c1.display()