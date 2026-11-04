""" 
Write a recursive function called reverse which accepts a string and returns a new string in reverse.

Examples

    reverse('python') # 'nohtyp'
    reverse('appmillers') # 'srellimppa'
"""

def reverse(string): 
    assert str(string), 'The input must be string type only'
    if len(string) <= 1: 
        return string
    return reverse(string[1:]) + string[0] 


print(reverse('python'))