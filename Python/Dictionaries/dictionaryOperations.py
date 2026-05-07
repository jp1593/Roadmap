# Dictionary operations and Functions

# IN/NOT = allows to check if a key exist in a dictionary
dictionary = { 7:"seven", 1:"one", 2:"two", 3:"three", 6:"six", 4:"four", 5:"five",}
# For keys
print(2 in dictionary)
# For values
print('seven' in dictionary.values())

# len() = count the number of pairs in the dictionary (it takes each pair as one element) 
print(len(dictionary))

# all() = checks the keys of the dictionary, if all keys are true it will return true (non-zero, non-empty, or not None), otherwise it will return false (like 0, "", or False)
print(all(dictionary))

# any()
print(any(dictionary))

# sorted() = return the list of keys but sorted
print(sorted(dictionary))