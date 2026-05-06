""" Dictionary creation """
my_dictionary = dict()
print(my_dictionary)

second_dictionary = {}
print(second_dictionary)

# Using dict constructor
eng_spanish = dict(one="uno", two="dos", three="tres", four="cuatro")
print(eng_spanish)

# Using only curly braces
eng_spanish2 =  {"one":"uno", "two":"dos", "three":"tres", "four":"cuatro"} 
print(eng_spanish2)

# Using dictionary constructor + list of tuples
eng_spanish_list =  [("one","uno"), ("two","dos"), ("three","tres"), ("four","cuatro")] 
eng_spanish3 = dict(eng_spanish_list)
print(eng_spanish3)

""" Dictionary update / addition of an element """
add_dict = {'name': 'Jhonson', 'age': 30}
# Change of value related to a key
add_dict["age"] = 22
# Addition of a value and its key
add_dict['address'] = 'Germany'
print(add_dict)

""" Traversing trough a dictionary """
def traversingDict(dictionary): 
    for key in dictionary: 
        print(key, dictionary[key])

traversingDict(add_dict)

""" Linear Search - Searching for a element in the dictionary """
def linearSearch(dictionary, value): 
    for key in dictionary: 
        if dictionary[key] == value: 
            return key, value
    return "Value don't exist"

print(linearSearch(add_dict, 22))

