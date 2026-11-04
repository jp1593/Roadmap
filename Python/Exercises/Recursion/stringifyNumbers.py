""" 
Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and converts them to strings. Recursion would be a great way to solve this!

Examples

    obj = {
      "num": 1,
      "test": [],
      "data": {
        "val": 4,
        "info": {
          "isRight": True,
          "random": 66
        }
      }
    }
     
    stringifyNumbers(obj)
     
    {'num': '1', 
     'test': [], 
     'data': {'val': '4', 
              'info': {'isRight': True, 'random': '66'}
              }
    }
"""

obj = {
    "num": 1,
    "test": [],
    "data": {
    "val": 4,
    "info": {
        "isRight": True,
        "random": 66
    }
    }
}

def stringifyNumbers(obj): 
    for key, val in dict.items(obj): 
        if isinstance(val, dict): 
            stringifyNumbers(val)
        else: 
            if isinstance(val, int) and not isinstance(val, bool): 
                obj[key] = str(val)
    return obj 

print(stringifyNumbers(obj))