data = [1,2,3,4,5,6,7,89,10]
print(data)
result = {item: item*item for item in data}
print(result)

result = {item:"ODD" if item%2 else "EVEN" for item in data}
print(result)