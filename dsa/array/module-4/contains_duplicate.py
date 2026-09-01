def contains_duplicate(arr,k):
    window = set()
    for i in  range (len(arr)):
        if arr[i] in window:
            return True

        window.add(arr[i])

        if len(window)>k:
           window.remove(arr[i-k])
            
    return False
nums = [1,2,3,1]
k = 3
print(contains_duplicate(nums,k))