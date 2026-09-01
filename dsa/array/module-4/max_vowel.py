def max_vowel(s,k):
  max_vowel = 0
  for i in range(k):
    if s[i] in "aeiou":
      max_vowel += 1
  count = max_vowel
  for i in range(k,len(s)):
     if s[i] in "aeiou":
       count += 1
     if s[i-k] in "aeiou":
       count -= 1
     if count > max_vowel:
       max_vowel = count    
  return max_vowel

s = "abciiidef"
k = 3
print(max_vowel(s,k))