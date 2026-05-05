"""
Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

Example

    pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
    Output : ['2+5', '4+3', '3+4', '-2+9']


Note:

4+3 comes from second and third elements from the main list.

3+4 comes from third and seventh elements from the main list.
"""

exercise_array = [2,4,3,5,6,-2,4,7,8,9]

target_value = 7 

def pair_sum(myList, sum): 
    array_review = myList.copy()
    pair_sums = []
    for i in range(len(array_review)): 
        base_number = array_review.pop(0)
        for j in range(len(array_review)): 
            if base_number + array_review[j] == sum: 
                pair_sums.append(f"{base_number}+{array_review[j]}")
    return pair_sums

pair_sum(exercise_array, target_value)
