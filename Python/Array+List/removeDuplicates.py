"""
Write a function to remove the duplicate numbers on given integer array/list.

Example

    remove_duplicates([1, 1, 2, 2, 3, 4, 5])
    Output : [1, 2, 3, 4, 5]
"""

exercise_array = [1, 1, 2, 2, 3, 4, 5]

def remove_duplicates(given_array): 
    no_duplicates = []
    for i in given_array:
        if i not in no_duplicates: 
            no_duplicates.append(i)
    return no_duplicates
        

print(remove_duplicates(exercise_array))