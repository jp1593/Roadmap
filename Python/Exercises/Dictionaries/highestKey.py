"""
Key with the Highest Value

Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

Example:

    my_dict = {'a': 5, 'b': 9, 'c': 2}
    max_value_key(my_dict))

Output:
b 
"""

my_dict = {'a': 5, 'b': 9, 'c': 2}

def max_value_key(my_dict):
    it = iter(my_dict)
    first_key = next(it)

    highest_key = first_key
    highest_value = my_dict[first_key]
    for key,value in my_dict.items(): 
        if value > highest_value: 
            highest_value = value
            highest_key = key
    return highest_key
            

print(max_value_key(my_dict))
