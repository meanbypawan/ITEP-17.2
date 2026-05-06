'''
  Nested Class :-

'''

class Outer:
    class Inner:
        def wish(self):
            print("GM.......")

# outer = Outer()
# inner = outer.Inner()
# inner.wish()            

inner = Outer.Inner()
inner.wish()