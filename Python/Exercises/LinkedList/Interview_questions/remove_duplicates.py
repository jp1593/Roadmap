""" 
Remove Duplicates
Write a function to remove duplicates from an unsorted linked list. Input 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 Output 1 -> 2 -> 3 -> 4 -> 5 
""" 


from LinkedListInterview import LinkedList

def remove_duplicates(ll):
    numbers = set()
    current_node = ll.head 
    previous_node = None
    while current_node is not None: 
        if current_node.value in numbers: 
            previous_node.next = current_node.next 
            if current_node == ll.tail: 
                ll.tail = previous_node
        else: 
            numbers.add(current_node.value)
            previous_node = current_node
        current_node = current_node.next 
    return ll

linked_list = LinkedList()
linked_list.generate(10, 1, 5)
print(linked_list)
remove_duplicates(linked_list)
print(linked_list)