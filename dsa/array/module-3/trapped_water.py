
def trap_water(arr):
        maxL = [0]*len(arr)
        maxR = [0]*len(arr)
        
        left_side_max = arr[0]
        maxL[0] = left_side_max
        for i in range(1,len(arr)):
           if arr[i] > left_side_max:
             left_side_max = arr[i]
           maxL[i] = left_side_max

        right = len(arr)-1 
        right_side_max = arr[right]
        maxR[right] = right_side_max
        for i in range(right-1,-1,-1):
            if arr[i] > right_side_max:
                right_side_max = arr[i]
            maxR[i] = right_side_max

        total_unit = 0
        for i in range(len(arr)):
           min = maxL[i] if maxL[i] < maxR[i] else maxR[i]
           total_unit += (min-arr[i])
        return total_unit
height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(height)

result = trap_water(height)

print(result)
