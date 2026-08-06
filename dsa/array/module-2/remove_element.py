def remove_element(numbers,val):
    pointerIndex = 0
    for i in range(len(numbers)):
        if numbers[i] != val:
            numbers[pointerIndex] = numbers[i]
            pointerIndex += 1

    return pointerIndex        

numbers = [3,2,2,3,4,5,6,7,3,3,8]
val = 3
print(numbers)
k = remove_element(numbers,val)
print(numbers[0:k])