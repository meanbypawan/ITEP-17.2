l1 = [1,4,6,6,7,7,8,8,8,9,10,15,20,21,26]
#   i=0,1,2,3,4 
l2 = [1,2,4,5,5,8,8,9,10]
#   j=0,1,2,3,4,5,6
# union :- [1,2,4,5,6,7,8,9,10]

n1 = len(l1)
n2 = len(l2)
result = []
i = j = 0
while i<n1 and j<n2:
  if l1[i] < l2[j]:
    if not result or result[-1]!=l1[i]:
      result.append(l1[i])
    i += 1
  elif l2[j] < l1[i]:
    if not result or result[-1] != l2[j]:
     result.append(l2[j])
    j += 1
  else:
    if not result or result[-1] != l1[i]:
     result.append(l1[i])
    i += 1
    j += 1

while i < n1:
    if not result or result[-1]!= l1[i]:
     result.append(l1[i])    
    i += 1

while j < n2:
    if not result or result[-1]!=l2[j]:
     result.append(l2[j])
    j += 1    

print(f"Union : {result}")        
