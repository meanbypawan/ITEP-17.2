def max_ons(arr,k):
    i = 0
    zeros = 0
    ans = 0
    for j in range(len(arr)):
      if arr[j] == 0:
         zeros+=1
      while zeros > k:
         if arr[i] == 0:
            zeros -= 1
         i += 1   
      ans = max(ans,(j-i+1))
    return ans
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(max_ons(nums,k))