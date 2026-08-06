# space :- O(1)
# Time : - O(n*n)
def duplicate_zero(numbers):
    i = 0
    while i < len(numbers):
        if numbers[i] == 0:
            for j in range(len(numbers)-1,i,-1):
                numbers[j] = numbers[j-1]
            numbers[j] = 0
            i += 2
        else:
            i+=1        

numbers = [1,0,2,3,0,4,5,0]
print(numbers)
duplicate_zero(numbers)
print(numbers)