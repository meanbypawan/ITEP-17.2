def min_size_array_sum(arr,target):
    i = 0
    current_sum = 0
    min_length = float('inf')
    for j in range(len(arr)):
        current_sum = current_sum + arr[j]
        while current_sum >= target:
            min_length = min(min_length,j-i+1)
            current_sum = current_sum - arr[i]
            i+=1
    return 0 if min_length == float('inf') else min_length        

#nums = [2,3,1,2,4,3]
nums = [1,1,1,1,1,1,1,1]
target = 11

print(min_size_array_sum(nums,target))