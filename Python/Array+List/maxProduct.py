"""
Find the maximum product of two integers in an array where all elements are positive.
"""

arr = [1, 7, 3, 4, 9, 5] 

def maxProduct(arr): 
    sorted_array = sorted(arr)
    first_number = sorted_array[-2]
    second_number = sorted_array[-1]
    return(first_number*second_number)

print(maxProduct(arr)) # Output: 63 (9*7)