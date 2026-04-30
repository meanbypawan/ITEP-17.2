def length_of_last_word(s):
    i = len(s)-1
    counter = 0
    
    while s[i] == " ":
        i-=1
    
    while s[i]!=" ":
        counter += 1
        i -= 1
    return counter;


result = length_of_last_word(" Python is sssimple     ")
print(f"{result}")