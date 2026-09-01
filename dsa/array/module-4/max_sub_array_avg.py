def max_average(arr,k):
    max_sum = 0
   
    for i in range(k):
        max_sum = max_sum + arr[i]

    current_sum = max_sum
    for i in range(k,len(arr)):
        current_sum = current_sum + arr[i] - arr[i-k]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum/k
        
nums = [1,12,-5,-6,50,3]
k = 4
print(f"Average : {max_average(nums,k)}")