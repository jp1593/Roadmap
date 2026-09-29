class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue: 
    def __init__(self):
        self.head = None 
        self.tail = None
        self.length = 0 

    def enqueue(self, value): 
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node 
            self.tail = new_node
        else: 
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1

my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)
