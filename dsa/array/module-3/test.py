class Solution:
    def numSubarrayProductLessThanK(self, arr, k):
        product = 1
        i = 0
        count = 0
        for j in range(len(arr)):
            if arr[j] < k:
                count += 1
        for j in range(len(arr)):
            product = product * arr[j]
            if product < k:
                count += 1
            else:
               while product >= k:
                  product = product / arr[i]
                  i += 1
        return count               

obj = Solution()
nums = [10,5,2,6]
k = 100    
print(obj.numSubarrayProductLessThanK(nums,k))
