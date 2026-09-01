def replacement(s,k):
    frequency = {}
    max_f = 0
    i = 0
    ans = 0
    for j in range(len(s)):
        frequency[s[j]]  = frequency.get(s[j],0) + 1
        max_f = max(max_f,frequency[s[j]])
        if (j-i+1) - max_f > k:
            ch = s[i]
            frequency[ch] -= 1
            i += 1
        ans = max(ans,j-i+1)
    return ans  

s = "AABABBA"
k = 1
print(replacement(s,k))