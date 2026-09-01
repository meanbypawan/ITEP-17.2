def findAnagrams(s,p):
    result = []
    need = {}
    for ch in p:
        need[ch] = need.get(ch,0) + 1
    window = {}
    i = 0
    for j in range(len(s)):
        window[s[j]] = window.get(s[j],0)+1
        if (j-i+1) > len(p):
            ch = s[i]
            window[ch] -= 1
            if window[ch] == 0:
                del window[ch]
            i += 1
        if need == window:
            result.append(i)
    return result                    
s = "cbaebabacd"
p = "abc"
print(findAnagrams(s,p))