class Stack:
    def __init__(self,size):
        self.stack = [None] * size
        self.top = -1

    def push(self,element):
        if self.top != len(self.stack)-1:
            self.top += 1
            self.stack[self.top] = element 
        else:
            print("Overflow...")

    def pop(self):
        if self.top != -1:
           element = self.stack[self.top]
           self.top -= 1
           return element
        else:
            print("Underflow...")

    def underflow(self):
        return self.top == -1                        

str = input("Enter some text : ")
s = Stack(50)

for ch in str:
    s.push(ch)

result = ""

while not s.underflow():
    result = result+s.pop()

print(result)        