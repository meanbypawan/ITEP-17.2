def fact(n):
    if n == 1: # Base Part / Termination Condition
        return 1
    return n * fact(n-1) # General Part / Recursive call statement

n = int(input("Enter a number : "))
result = fact(n)

print(f"Factorial of {n} is {result}")