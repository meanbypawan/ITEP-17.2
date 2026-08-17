class Stack:
    def __init__(self,size):
        self.stack = [None] * size
        self.top = -1
    
    def is_overflow(self):
        return self.top == len(self.stack)-1

    def is_underflow(self):
        return self.top == -1
    
    def push(self,element):
        if not self.is_overflow():
            self.top += 1
            self.stack[self.top] = element
        else:
            print("Stack is overflow...")    

    def pop(self):
        if not self.is_underflow():
            element = self.stack[self.top]
            self.top -= 1
            print(f"{element} removed...")
        else:
          print("Stack is underflow...")

    def peek(self):
       if not self.is_underflow():
           return self.stack[self.top]
       
    def traverse(self):
      if not self.is_underflow():  
        for i in range(self.top,-1,-1):
            print(self.stack[i])
      else:
          print("Stack underflow...")   
             
s = Stack(5)
while True:
    print("1 for push")
    print("2 for pop")
    print("3 for peek")
    print("4 for traverse")
    print("5 for exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        element = int(input("Enter element : "))
        s.push(element)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.traverse()
    else:
        break                