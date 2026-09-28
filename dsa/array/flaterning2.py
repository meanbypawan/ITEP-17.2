arr = [1,2,[3,4,[5,6]]]
result = []
for element in arr:
    if isinstance(element,list):
       result.extend(element.flatten())
    else:
        result.append(element)   
print(result)        