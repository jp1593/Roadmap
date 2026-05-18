"""Tuple Operations / Functions"""
firstTuple = (1,2,3,4,5)
secondTuple = (1,2,8,9,10,7)
print(firstTuple+secondTuple)
print(firstTuple*2)

# .count() method
print(firstTuple.count(2))

# .index() method
print(secondTuple.index(9))

# len() function
print(len(firstTuple))

# max() function
print(max(secondTuple))

# min() function
print(min(firstTuple))

# tuple() function, converts a list to a tuple
print(tuple([1,2,3,4,5,6]))