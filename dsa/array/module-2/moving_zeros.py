def moving_zeros(nummbers):

    pointerIndex = 0
    for i in range(len(numbers)):
        if numbers[i]!=0:
            numbers[pointerIndex],numbers[i] = numbers[i],numbers[pointerIndex]
            pointerIndex+=1

    
numbers = [0,0,0,0,1,5,6,7,0,1,0,0,0,0,3,0,0,0,0,12,0,0]

print(numbers)
moving_zeros(numbers)
print(numbers)