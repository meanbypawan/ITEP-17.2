def calc(a,b,op):
    if op == "+":
        return b + a
    elif op == "-":
        return b - a
    elif op == "*":
        return b * a
    elif op == "/":
        return b / a
    
def postfix_evalution(arr):
    stack = []
    for element in arr:
        if element.lstrip("-").isnumeric():
            stack.append(element)
        else:
            a = stack.pop()
            b = stack.pop()
            ans = calc(int(a),int(b),element)
            stack.append(ans)
    return stack.pop()        

#tokens = ["2","1","+","3","*"]
#tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["4","13","5","/","+"]
print(postfix_evalution(tokens))
