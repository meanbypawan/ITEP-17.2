def valid_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        # Moving left pointer
        while left < len(s) and not s[left].isalnum():
            left += 1
        # Moving right pointer
        while right >= 0 and not s[right].isalnum():
            right -= 1

        if s[left] != s[right]:
          return False
        left += 1
        right -= 1

    return True                 

#s = ",,,..Ma.,,,d,,a,,,M"
s = ",,,1...22,1"
result = valid_palindrome(s)
print(result)