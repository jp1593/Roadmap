"""
Implement and algorithm to finde the nth to last element of a singly linked list

This means: Return the element that is N steps from the last element 
"""

from LinkedListInterview import LinkedList

def reverse(ll): 
    current_node = ll.head 
    previous_node = None
    ll.tail = ll.head
    while True: 
        next_node = current_node.next 
        current_node.next = previous_node 
        previous_node = current_node 
        current_node = next_node 
        if current_node is None: 
            break 
    ll.head = previous_node
    return ll

def return_NthLast(ll, nth): 
    if ll.head is None or nth < 0 or nth > len(ll): 
        return None
    reverse(ll)
    target_node = ll.head
    for _ in range(nth-1): 
        target_node = target_node.next 
    reverse(ll)
    return target_node

linked_list = LinkedList()
linked_list.generate(10, 1, 5)
print(linked_list)
print(return_NthLast(linked_list,10))
print(linked_list)