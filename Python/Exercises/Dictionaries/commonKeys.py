"""
Common Keys

Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:

    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    merge_dicts(dict1, dict2)

Output:

    {'a': 1, 'b': 5, 'c': 7, 'd': 5}
"""


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dicts(dict1, dict2):
    merge_dict = dict1.copy()

    for key in dict2: 
        if key in merge_dict: 
            merge_dict[key] += (dict2[key])
        else: 
            merge_dict[key] = (dict2[key])
    return merge_dict

print(merge_dicts(dict1, dict2))
