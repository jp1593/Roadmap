
myDict = {"name":"Edy", "age":22, "address":"Germany", "status":"available"}
print(myDict)

# .copy() = returns a shallow copy of dictionary
dictCopy = myDict.copy()
print(dictCopy)

# .clear() = eliminates all the key value pairs of the dictionary 
myDict.clear()
print(myDict)

#  .fromkeys() = creates new dictionary from a given sequence of elements with value provided by user
newDict = {}.fromkeys([1,2,3,4], 0,)
print(newDict)

# .get() = returns the value of specified key if the key is in the dictionary.
print(dictCopy.get("status"))

# .items() = returns a view object that displays a list of dictionaries, key value tuple pairs. 
print(dictCopy.items())

# .keys() = returns a view object that displays all keys in the dictionary. 
print(dictCopy.keys())

# .popitem() = removes the last element of the dictionary; works as the same way in which pop() works in arrays
dictCopy.popitem()
print(dictCopy)

# .setdefault() = returns the value of key if key is in the dictionary, if not, it inserts key with a value to the dictionary.
dictCopy.setdefault("account", 1010101)
print(dictCopy)

# .pop() = removes and returns an element from the dictionary having a given key. 
dictCopy.pop("address")
print(dictCopy)

# .values() = returns a view object that display a list of values in the dictionary
print(dictCopy.values()) 

# .update() = updates the dictionary with the elements from another dictionary object or from an iterable of key value pairs, it adds elements to the dictionary if the key isn’t in the dictionary. 
updateDict = {"name":"Carl"}
dictCopy.update(updateDict)
print(dictCopy)

dictCopy.update({'name':'Edy'})
print(dictCopy)