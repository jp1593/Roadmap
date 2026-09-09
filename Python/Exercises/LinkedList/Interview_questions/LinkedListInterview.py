from random import randint

class Node: 
    def __init__(self, value=None):
        self.value = value 
        self.next = None 
        self.previous = None

    def __str__(self):
        return str(self.value)

class LinkedList: 
    def __init__(self, value=None): 
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head 
        while current_node: 
            yield current_node 
            current_node = current_node.next 

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' <-> '.join(values)

    def __len__(self):
        result = 0 
        node = self.head 
        while node: 
            result += 1
            node = node.next 
        return result

    def add(self, value): 
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node 
            self.tail = new_node
        else: 
            new_node.previous = self.tail
            self.tail.next = new_node 
            self.tail = new_node  
        return self.tail 

    def generate(self, n, min_value, max_value): 
        self.head = None 
        self.tail = None 
        for i in range(n): 
            self.add(randint(min_value, max_value))
        return self

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(len(customLL))