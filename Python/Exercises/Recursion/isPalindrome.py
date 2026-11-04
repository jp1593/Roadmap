""" 
Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads the same forward and backward). Otherwise it returns false.

Examples

    isPalindrome('awesome') # false
    isPalindrome('foobar') # false
    isPalindrome('tacocat') # true
    isPalindrome('amanaplanacanalpanama') # true
    isPalindrome('amanaplanacanalpandemonium') # false
"""

def isPalindrome(strng): 
    assert str(strng), 'The input must be string type only'
    if len(strng) <= 1:
        return True
    if strng[0] != strng[-1]:
        return False
    return isPalindrome(strng[1:-1])

print(isPalindrome('awesome')) # false
print(isPalindrome('foobar')) # false
print(isPalindrome('tacocat')) # true