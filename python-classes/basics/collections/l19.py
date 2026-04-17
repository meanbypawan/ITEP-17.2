l1 = [1,4,6,6,7,7,8,8,8,9,10,15,20,21,26]
l2 = [1,2,4,5,5,8,8,9,10,26]
l3 = [1,8,10,15,16,26]
n1 = len(l1)
n2 = len(l2)
n3 = len(l3)
result = []
i = j = k = 0
print(f"L1 : {l1}")
print(f"L2 : {l2}")
print(f"L3 : {l3}")
while i < n1 and j < n2 and k < n3:
    if l1[i] == l2[j] == l3[k]:
        if len(result)==0 or result[-1] != l1[i]:
          result.append(l1[i])
        i += 1
        j += 1
        k += 1  
    elif l1[i] < l2[j] and l1[i] < l3[k]:
        i += 1
    elif l2[j] < l3[k]:
        j += 1
    else:
        k += 1        
print(f"Result : {result}")            