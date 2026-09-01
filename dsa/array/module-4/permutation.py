def checkInclusion(s1,s2):

    frequency_count = {}

    for ch in s1:
        frequency_count[ch] = frequency_count.get(ch,0)+1
    
    i = 0
    window = {}
    for j in range(len(s2)):
      window[s2[j]] = window.get(s2[j],0) + 1

      if (j-i+1) > len(s1):
         ch = s2[i]
         window[ch] -= 1
         if window[ch] == 0:
            del window[ch]
         i += 1 
      if frequency_count == window:
         return True     
    return False        

s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1,s2))