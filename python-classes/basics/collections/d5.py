# Count the occurange of each number

data = [10,20,3,5,10,6,7,8,9,10,5,7,3,3,3]

result = {}
for item in data:
   result[item] =  result.get(item,0) + 1

# for item in data:
#     if result.get(item):
#         result[item] = result[item] + 1
#     else:
#         result[item] = 1    
print(f"Result : {result}")        