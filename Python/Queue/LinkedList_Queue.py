class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linkedList]
        return " -> ".join(values)

    def isEmpty(self):
        return self.linkedList.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = new_node
            self.linkedList.tail = new_node
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node

    def isEmpty(self): 
        return self.linkedList.head == None 

    def dequeue(self): 
        if self.isEmpty():
            return "The Queue doesn't have any element"
        else: 
            removed_node = self.linkedList.head 
            if self.linkedList.head == self.linkedList.tail: 
                self.linkedList.head = None
                self.linkedList.tail = None
            else: 
                self.linkedList.head = self.linkedList.head.next
                removed_node.next = None 
        return removed_node

my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)
print(my_queue)
my_queue.dequeue()
print(my_queue)