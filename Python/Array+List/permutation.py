"""
Given two strings write a method to decide if one is permutation of another.
"""

def permutation(first_list, second_list): 
    if len(first_list) != len(second_list): 
        return False
    first_list.sort()
    second_list.sort()
    if first_list == second_list: 
        return True
    else: 
        return False
    
first_list = [1,2,3,4]
second_list = [4,1,3,2]

print(permutation(first_list, second_list))