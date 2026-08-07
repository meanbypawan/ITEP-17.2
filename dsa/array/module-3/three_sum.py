def threeSum(numbers):
    numbers.sort()
    triplets = []
    for i in range(len(numbers)-2):
      if i==0 or numbers[i]!=numbers[i-1]:
        twoSum(numbers,i,triplets)

    return triplets
def twoSum(numbers,i,triplets):
    left = i + 1
    right = len(numbers)-1
    while left < right:
        sum = numbers[left] + numbers[right] + numbers[i]
        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            triplets.append([numbers[i],numbers[left],numbers[right]])
            left += 1
            right -= 1        

            while left < right and numbers[left] == numbers[left-1]:
                left += 1
            while right >= 0 and numbers[right] == numbers[right+1]:
                right -= 1

numbers = [-1,0,1,2,-1,-4]
triplets = threeSum(numbers)
print(triplets)