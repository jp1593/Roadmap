""" 
Write a recursive function called capitalizeWords. Given an array of words, return a new array containing each word capitalized.

Examples

    words = ['i', 'am', 'learning', 'recursion']
    capitalizeWords(words) # ['I', 'AM', 'LEARNING', 'RECURSION']
"""
words = ['i', 'am', 'learning', 'recursion']

def capitalizeWords(arr): 
    if len(arr) == 0: 
        return []
    if len(arr) == 1: 
        return [arr[0].upper()]
    return [arr[0].upper()] + capitalizeWords(arr[1:])

print(capitalizeWords(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']