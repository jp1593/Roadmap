def fibonacci(n): 
    assert n>=0 and int(n) == n, 'Fibonacci number must be positive integer only'
    if n == 0 or n == 1: 
        return n
    else: 
     return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))