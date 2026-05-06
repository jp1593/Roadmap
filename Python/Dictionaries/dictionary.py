# Dictionary creation
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