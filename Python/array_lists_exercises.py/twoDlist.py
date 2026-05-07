"""
Given 2D list calculate the sum of diagonal elements.

Example

    myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
     
    diagonal_sum(myList2D) # 15
"""

myList2D=[[1,2,3],[4,5,6],[7,8,9]] 

def diagonal_sum(matrix): 
    if not matrix: 
        return 0
    
    columns_amount = len(matrix[0])
    rows_amount = (len(matrix))
    counter = 0
    diagonal_values = []
    if columns_amount == rows_amount: 
        while counter < len(matrix): 
            diagonal_values.append(matrix[counter][counter])
            counter += 1
    else: 
        return("This isn't a square matrix")
    return sum(diagonal_values)

print(diagonal_sum(myList2D))
