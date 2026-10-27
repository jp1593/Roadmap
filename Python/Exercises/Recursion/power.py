"""
Calculate the power of a number using recursion
"""

def power(base, exponent):
    assert int(exponent) == exponent, 'The exponent must be integer number only'
    if exponent < 0:
        return 1 / power(base, -exponent)
    if exponent == 0: 
        return 1
    return base * power(base, exponent-1)

print(power(5, 3))