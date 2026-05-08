class Test:
    def __new__(cls):
        print("__new__ called....")
        return super().__new__(cls)    
    
    def wish(self):
        print("Wow.....")

obj = Test()
obj.wish()

