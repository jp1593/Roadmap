"""
Write a program to find all pairs of integers whose sum is equal to a given number

Ex: [2,6,3,9,11] Target: 9 Answer: [6,3]

Additional information: 
- Same numbers aren't a valid pair (2,2) (3,3)
- 
"""

given_array = [2,6,3,9,11]

def pairValidation(given_array, target): 
    array_result = []
    for i in range(len(given_array) - 1):
        if (given_array[i] + given_array[i+1]) == target and given_array[i] != given_array[i+1]: 
            array_result.append([given_array[i], given_array[i+1]])
    return array_result


print(pairValidation(given_array, 9))