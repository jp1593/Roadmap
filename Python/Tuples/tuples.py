"""Creation of tuples"""
# Tuple Creation
newTuple = ('a', 'b', 'c', 'd', 'e')
print(newTuple)

# Built-in tuple function
anotherTuple = tuple('abcde')
print(anotherTuple)

"""Accessing tuple values"""
# Acessing b
print(newTuple[1])

# Acessing e
print(newTuple[-1])

# Slicing
print(newTuple[1:3])

# Linear search
for i in newTuple: 
    print(i)

# Acessing by index
for i in range(len(newTuple)): 
    print(newTuple[i])

# Searching for specific values in tuple
print('b' in newTuple)

# Searching for index of specific value
print(newTuple.index('a'))

# Manual search
def searchTuple(inp_tuple, target): 
    for i in range(len(inp_tuple)): 
        if inp_tuple[i] == target: 
            return f"Value:{target}, Index: {i}"
    return "Element not in tuple"

print(searchTuple(newTuple, 'a'))