"""
Write a code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x
"""



from LinkedListInterview import LinkedList

def partition(ll, x): 
    current_node = ll.head
    ll.tail = ll.head 

    while current_node: 
        nextNode = current_node.next 
        current_node.next = None
        if current_node.value < x:
            current_node.next = ll.head 
            ll.head = current_node 
        else: 
            ll.tail.next = current_node 
            ll.tail = current_node 
        current_node = nextNode

    if ll.tail.next is not None: 
        ll.tail.next = None 


linked_list = LinkedList()
linked_list.generate(10, 1, 5)
partition(linked_list, 10)
print(linked_list)
partition(linked_list, 4)
print(linked_list)