"""
You have two numbers represented by a linked list, where each node contains a single digit. 

The digits are store in reverse order, such that the 1's digit is at the head of the list. 

Write a function that adds the two numbers and return the sum as a linked list. 
"""

from LinkedListInterview import LinkedList

def sumList(l1, l2): 
    new_list = LinkedList()
    if l1 is None or l2 is None: 
        return None
    carry = 0 
    l1_node = l1.head 
    l2_node = l2.head 
    while l1_node or l2_node or carry:  
        first_value = 0
        second_value = 0 

        if l1_node is None: 
            first_value = 0
        else:
            first_value = l1_node.value 

        if l2_node is None: 
            second_value = 0
        else: 
            second_value = l2_node.value 

        total = first_value + second_value + carry

        carry = total // 10 
        total = total % 10

        new_list.add(total)

        if l1_node: 
            l1_node = l1_node.next 
        
        if l2_node: 
            l2_node = l2_node.next 

    return new_list


first_linked_list = LinkedList()
second_linked_list = LinkedList()
first_linked_list.generate(3, 9, 9)
second_linked_list.generate(3, 9, 9)
print(f"First list; {first_linked_list}, Second list; {second_linked_list}")
print(sumList(first_linked_list, second_linked_list))
