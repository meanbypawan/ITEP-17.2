def sorted_square(numbers):
    result = [0]*len(numbers)
    # [0,0,0,0,0]
    left = 0
    right = len(numbers) - 1
    for i in range(len(result)-1,-1,-1):
        if abs(numbers[left]) > abs(numbers[right]):
            result[i] = numbers[left]*numbers[left]
            left += 1
        else:
            result[i] = numbers[right] * numbers[right]
            right -= 1    
    return result

numbers = [-4,-1,0,3,10]
print(numbers)
result = sorted_square(numbers)
print(result)