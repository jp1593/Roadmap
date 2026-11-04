"""
collectStrings

Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string.

Examples

    obj = {
      "stuff": 'foo',
      "data": {
        "val": {
          "thing": {
            "info": 'bar',
            "moreInfo": {
              "evenMoreInfo": {
                "weMadeIt": 'baz'
              }
            }
          }
        }
      }
    }
     
    collectStrings(obj) # ['foo', 'bar', 'baz']
"""

obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}


def collectStrings(obj): 
    result = []
    for key, value in dict.items(obj): 
        if isinstance(value, dict): 
            result.extend(collectStrings(value))
        else: 
            if isinstance(value, str): 
                result.append(value)
    return result

print(collectStrings(obj))
