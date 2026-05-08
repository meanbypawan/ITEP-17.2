class Test:
    # def __init__(self,a):
    #     print("1 wala init......")
    #     print("a : {}".format(a))
    
    def __init__(self,a,b=100):
        print("2 wala init.....")
        print("a : {}, b : {}".format(a,b))
        return "Hello....."


obj = Test(10)
obj.__init__(200,100)
