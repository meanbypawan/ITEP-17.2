s = "aaabbbcccddddeeffffffggghhi"
result = {}

for ch in s:
    result[ch] = result.get(ch,0) + 1

print(result)    
