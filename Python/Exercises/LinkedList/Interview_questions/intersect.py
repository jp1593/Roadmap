"""
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node

Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list
is the same exact same node (by reference) as the jth node of the second linked list, then they are intersecting. 
"""
from LinkedListInterview import LinkedList, Node
from random import randint

def intersect(l1, l2): 
    if l1.tail is not l2.tail: 
        return False
   
    len1 = len(l1)
    len2 = len(l2)

    shorter = l1 if len1 < len2 else l2 
    longer = l2 if len1 < len2 else l1

    diff = len(longer) - len(shorter)

    longerNode = longer.head 
    shorterNode = shorter.head 

    for i in range(diff): 
        longerNode = longerNode.next 

    while shorterNode is not longerNode: 
        shorterNode = shorterNode.next 
        longerNode = longerNode.next 
    return longerNode

# 1. Create List A: 3 -> 1 -> 5 -> 9
listA = LinkedList()
listA.add(3)
listA.add(1)
listA.add(5)
listA.add(9)

# 2. Create List B: 2 -> 4 -> 6
listB = LinkedList()
listB.add(2)
listB.add(4)
listB.add(6)

# 3. Create the intersecting portion starting with the node holding '7'
intersecting_node = Node(randint(1, 9))
intersecting_node.next = Node(randint(1, 9))
intersecting_node.next.next = Node(randint(1, 9)) 

# 4. Attach the exact same node reference to both lists
listA.tail.next = intersecting_node
listA.tail = intersecting_node.next.next  # update tail to the node with '1'

listB.tail.next = intersecting_node
listB.tail = intersecting_node.next.next  # update tail to the node with '1'

print("List A:", listA)
print("List B:", listB)
print(intersect(listA, listB))