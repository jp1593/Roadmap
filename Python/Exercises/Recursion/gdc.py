"""
Find the GCD (Greates Common Divisor) of two numbers
"""

def gcd(a, b): 
    assert int(a) == a and int(b) == b, 'The numbers must be integer number only'
    if a < 0: 
        a = -1 * a 
    if b < 0: 
        b = -1 * b
    if b == 0: 
        return a 
    return gcd(b, a % b)


print(gcd(18, 12))