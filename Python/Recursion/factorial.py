def factorial(n):
    if n < 0: 
        raise ValueError("Factorial is only defined for positive numbers")
    if n < 1: 
        return 1 
    else: 
        return n * factorial(n-1)

print(factorial(10))