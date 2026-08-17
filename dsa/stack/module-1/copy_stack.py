class Stack:
    def __init__(self,size):
        self.stack = [None]*size
        self.top = -1

    def push(self,element):
        if self.top != len(self.stack)-1:
            self.top += 1
            self.stack[self.top] = element

    def pop(self):
       if self.top != -1:
           element = self.stack[self.top]
           self.top -= 1
           return element
        
    def underflow(self):
       return self.top == -1

    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i],end=" ")
        print("----------------------------------------")    
s1 = Stack(10)
s1.push(100)
s1.push(200)
s1.push(300)
s1.push(400)
s1.push(500)

s1.traverse()

temp = Stack(10)
while not s1.underflow():
    temp.push(s1.pop())

s2 = Stack(10)
while not temp.underflow():
    s2.push(temp.pop())    

s2.traverse()