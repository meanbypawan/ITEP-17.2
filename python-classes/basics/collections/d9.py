d = {"a":2,"b":1,"c":4,"d":3,"e":5}

l = list(d.items())

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i][1] > l[j][1]:
            l[i],l[j] = l[j],l[i]

print(f"Result : {dict(l)} len : {len(dict(l))}")