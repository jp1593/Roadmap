""" 
nestedEvenSum

Write a recursive function called nestedEvenSum. Return the sum of all even numbers in an object which may contain nested objects.

Examples

    obj1 = {
      "outer": 2,
      "obj": {
        "inner": 2,
        "otherObj": {
          "superInner": 2,
          "notANumber": True,
          "alsoNotANumber": "yup"
        }
      }
    }
     
    obj2 = {
      "a": 2,
      "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
      "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
      "d": 1,
      "e": {"e": {"e": 2}, "ee": 'car'}
    }
     
    nestedEvenSum(obj1) # 6
    nestedEvenSum(obj2) # 10
"""
def nestedEvenSum(obj, sum=0): 
    for key, val in obj.items():
        if isinstance(val, dict): 
            sum += nestedEvenSum(val)
        elif isinstance(val, int) and not isinstance(val, bool):  
            if val%2 == 0: 
                sum += val
    return sum 


obj1 = {
    "outer": 2,
    "obj": {
    "inner": 2,
    "otherObj": {
        "superInner": 2,
        "notANumber": True,
        "alsoNotANumber": "yup"
    }
    }
}
    
obj2 = {
    "a": 2,
    "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
    "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": 'car'}
}
    
print(nestedEvenSum(obj1)) # 6
print(nestedEvenSum(obj2)) # 10
