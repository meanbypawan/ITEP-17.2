A = [
    [1,2,3],
    [4,5,6]
]

B = [
    [1,2],
    [3,4],
    [5,6]
]

m,n,p,q = 2,3,3,2
result = []
for i in range(m):
    row = []
    for j in range(q):
        sum = 0
        for k in range(p):
          sum = sum + A[i][k] * B[k][j]
        else:
            row.append(sum)
    else:
        result.append(row) 

print(f"A : {A}")
print(f"B : {B}")
print(f"AXB : {result}")