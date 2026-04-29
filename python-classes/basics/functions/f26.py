
def extend_wish(func):
    def wrapper(name):
      if name == "Shikha":
        print(f"Good Afternoon...{name}")
      elif name == "Arpit":
        print(f"Hello {name}")
      else:
        func(name)    
    return wrapper    

@extend_wish
def wish(name):
    print(f" Good Morning {name}")


wish("Atul")
wish("Shikha")    
wish("Arpit")