def merge_array(arr1,arr2,m,n):
    i = m-1
    j = n-1
    position = m + n - 1
    while j >=0:
       if i >= 0 and arr1[i] > arr2[j]:
           arr1[position] = arr1[i]
           i -= 1
       else:
           arr1[position] = arr2[j]
           j -= 1
       position -= 1

#nums1=[1,2,3,0,0,0]
nums1 = [2,0]
#nums2=[2,5,6]
nums2 = [1]
m=1
n = 1
print(nums1)
print(nums2)
merge_array(nums1,nums2,m,n)
print(nums1)
