def precedence(op):
    if op in "+-":
        return 1
    elif op in "*/%":
        return 2
    return 0

def convert(infix):
    postfix = []
    stack = []
    for element in infix:
        if element.isalnum():
            postfix.append(element)

        elif element == "(":
            stack.append(element)

        elif element == ")":
            while stack and stack[-1]!="(":
                postfix.append(stack.pop())
            stack.pop()    
        else:
            while stack and precedence(stack[-1]) >= precedence(element):
                postfix.append(stack.pop())

            stack.append(element)        
    while stack:
        postfix.append(stack.pop())

    return "".join(postfix)    
infix = "((10*(6/((9+3)*11)))+17)+5"
postfix = convert(infix)
print(infix)
print(postfix)
