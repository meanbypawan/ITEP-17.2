def threeSumClosest(numbers,target):
    def twoSum(numbers,x):
        nonlocal closest
        left = x + 1
        right = len(numbers)-1
        while left < right:
            current_sum = numbers[left] + numbers[right] + numbers[x]

            if abs(current_sum - target) <  abs(closest - target):
                closest = current_sum

            elif current_sum < target:
                left += 1

            elif current_sum > target:
                right -= 1

            else:
                closest = current_sum
                return closest
    numbers.sort()

    closest = numbers[0] + numbers[1] + numbers[2]
    for i in range(len(numbers)-2):
        twoSum(numbers,i)

    return closest


#numbers = [0,0,0]
#numbers = [-1,-1,-1,2,2,2]
#numbers = [-1,2,1,-4]
#numbers = [-1000,-999,998,999,1000]
#numbers = [-10,-9,-8,-7,100]
numbers = [-5,-4,-3,-2,-1]
target = -8
triplets = threeSumClosest(numbers,target)
print(triplets)