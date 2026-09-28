result = []
output = []
def f1(arr): # [5,6]
    global result
    global output
    for element in arr:
        if isinstance(element,list):
            output.append(result)
            result = []
            return f1(element)
        else:
            result.append(element)
    else:
        output.append(result)            
    

arr = [1,2,[3,4,[5,6]]]
f1(arr)
print(output)