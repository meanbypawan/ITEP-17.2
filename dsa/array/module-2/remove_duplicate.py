def remove_duplicate(numbers):
    pointerIndex = 0
    for i in range(1,len(numbers)):
        if numbers[pointerIndex]!=numbers[i]:
            pointerIndex += 1
            numbers[pointerIndex] = numbers[i]
    return pointerIndex + 1

numbers = [1,1,2,2,3]

k = remove_duplicate(numbers)

print(numbers[0:k])