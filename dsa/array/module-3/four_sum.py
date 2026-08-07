def fourSum(numbers,target):
    quadruplet = []
    numbers.sort()
    for i in range(len(numbers)):
        if i == 0 or numbers[i]!=numbers[i-1]:
         threeSum(numbers,i,target,quadruplet)
    return quadruplet  

def threeSum(numbers,i,target,quadruplet):
    for j in range(i+1,len(numbers)-2):
      if j==1 or numbers[j]!=numbers[j-1]:
        twoSum(numbers,i,j,target,quadruplet)


def twoSum(numbers,i,j,target,quadruplet):
    left = j + 1
    right = len(numbers)-1
    while left < right:
        sum = numbers[left] + numbers[right] + numbers[i] + numbers[j]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            quadruplet.append([numbers[i],numbers[j],numbers[left],numbers[right]])
            left += 1
            right -= 1        

            while left < right and numbers[left] == numbers[left-1]:
                left += 1
            while right >= 0 and numbers[right] == numbers[right+1]:
                right -= 1

numbers = [1,0,-1,0,-2,2]
target = 0
quadruplet = fourSum(numbers,target)
print(quadruplet)