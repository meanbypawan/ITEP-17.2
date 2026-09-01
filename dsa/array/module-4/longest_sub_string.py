def longest_substring(s):
    window = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
      while s[right] in window:
         window.remove(s[left])
         left += 1

      window.add(s[right])
      if (right-left + 1) > max_length:
         max_length = right - left + 1 
    return max_length

s = "abcabcbb"

print(longest_substring(s))