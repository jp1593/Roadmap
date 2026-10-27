"""
Convert decimal number to a binary one
"""

def decimalToBinary(number):
    assert int(number) == number, 'The numbers must be integer number only'
    if number == 0: 
        return ""
    return decimalToBinary(number//2) + str(number%2) 

print(decimalToBinary(100))