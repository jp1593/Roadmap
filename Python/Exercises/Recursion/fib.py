"""
Write a recursive function called fib which accepts a number and returns the nth number in the Fibonacci sequence. 
Recall that the Fibonacci sequence is the sequence of whole numbers 0,1, 1, 2, 3, 5, 8, ... which starts with 0 and 1, and where every 
number thereafter is equal to the sum of the previous two numbers.

Examples

    fib(4) # 3
    fib(10) # 55
    fib(28) # 317811
    fib(35) # 9227465
"""

def fib(num):
    assert int(num) == num and num >= 0, 'The number must be integer number only'
    if num == 0: 
        return 0 
    if num == 1: 
        return 1 
    return fib(num-2) + fib(num-1)

print(fib(10))