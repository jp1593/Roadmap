"""
Write a function called recursiveRange which accepts a number and adds up all the numbers from 0 to the number passed to the function.

Examples

    recursiveRange(6) # 21
    recursiveRange(10) # 55 
"""

def recursiveRange(num): 
    assert int(num) == num and num >= 0, 'The number must be integer number only'
    if num == 0: 
        return 0 
    return num + recursiveRange(num-1) 

print(recursiveRange(6))