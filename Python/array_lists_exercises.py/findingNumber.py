"""
How to check if an array contains a number in Python
"""

import numpy as np 
exerciseArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

# Python capabilities
def findingNumber(exerciseArray, target): 
    exerciseSet = set(exerciseArray)
    if target in exerciseSet: 
        return("Number is in the array")
    else: 
        return("The Number isn't in the array")
    
print(findingNumber(exerciseArray, 15))

# Linear Search
def linearSearch(exerciseArray, target): 
    for i in exerciseArray: 
        if i == target: 
            return("The number is in the array")
        else: 
            return("The number is not in the array")

print(linearSearch(exerciseArray, 30))