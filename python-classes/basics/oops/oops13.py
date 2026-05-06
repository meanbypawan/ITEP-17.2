'''
 Methods:-
   instance
   static
   class Methods
Variables :-
  instance
  static varaible/class variable
  local
  global   
'''
class TestObjectCount:
    __counter = 0
    def __init__(self):
        TestObjectCount.__counter += 1
    
    @classmethod
    def get_total_count(cls):
        return TestObjectCount.__counter    

obj = TestObjectCount()
obj2 = TestObjectCount()
obj3 = TestObjectCount()

print(f"Total Object : {TestObjectCount.get_total_count()}")
















