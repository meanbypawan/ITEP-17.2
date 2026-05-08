class Test:
    def __new__(cls):
      print("__new__ called.....")  
      return super().__new__(cls)
   
    def __init__(self):
        print("init called.....")

obj = Test()
