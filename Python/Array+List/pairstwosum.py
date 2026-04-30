"""
Write a program to find all pairs of integers whose sum is equal to a given number

Ex: [2,6,3,9,11] Target: 9 Answer: [6,3]

Additional information: 
- Same numbers aren't a valid pair (2,2) (3,3)
- 
"""

#given_array = [2,6,3,9,11,7,0]
#given_array = [2,6,3]
given_array = [4,4,5,5]

def pairValidation(given_array, target): 
    function_array = given_array.copy()
    array_result = []
    base_number = 0
    for i in range(len(function_array)):
        base_number = function_array.pop(0)
        for j in range(len(function_array)):
            if base_number + function_array[j] == target and ([base_number, function_array[j]] not in array_result): 
                array_result.append([base_number, function_array[j]])
    return(array_result)

print(pairValidation(given_array, 9))