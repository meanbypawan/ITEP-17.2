'''
 Decorator :-
  Extend the functionality of a function
'''

def test_extend(func):
    def wrapper():
        print("Before executing test function")
        func()
        print("After executing test function")
    return wrapper    

@test_extend
def test():
    print("This is testing")

test()
# test_wrapper = test_extend(test)  
# test_wrapper()