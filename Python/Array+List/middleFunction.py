"""
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

"""

myList = [1, 2, 3, 4]
def middleFunction(input_list): 
    transform_list = input_list[1:-1]
    return(transform_list)

print(middleFunction(myList))