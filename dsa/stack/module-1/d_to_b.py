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
n = int(input("Enter decimal no : "))
s = Stack(100)

while n != 1:
    r = n%2
    n = n // 2
    s.push(r)

s.push(1)

result = ""
while not s.underflow():
    result = result + str(s.pop())
print(f"Binary : {result}")    