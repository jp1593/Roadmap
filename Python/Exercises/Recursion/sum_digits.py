"""
Find the sum of digits of a positive integer number using recursion
"""

def sumOfDigits(n): 
    assert n>=0 and int(n) == n, 'The number must be positive integer only'
    if n == 0: 
        return 0
    return n%10 + sumOfDigits(n//10)

print(sumOfDigits(112))