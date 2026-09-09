class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.previous = None

class CircularDoubleLinkedList: 
    def __init__(self):
        self.head = None 
        self.tail =  None 
        self.length = 0

    def append(self, value): 
        new_node = Node(value)
        if not self.head: 
            new_node.previous = new_node 
            new_node.next = new_node 
            self.head = new_node 
            self.tail = new_node 
        else: 
            new_node.previous = self.tail 
            new_node.next = self.head 
            self.head.previous = new_node
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1

    def prepend(self, value): 
        new_node = Node(value)
        if not self.head: 
            new_node.previous = new_node 
            new_node.next = new_node 
            self.head = new_node 
            self.tail = new_node 
        else: 
            self.head.previous = new_node 
            self.tail.next = new_node 
            new_node.next = self.head 
            new_node.previous = self.tail 
            self.head = new_node
        self.length += 1

    def traverse(self): 
        if not self.head: 
            return
        current_node = self.head 
        while True: 
            print(current_node.value)
            current_node = current_node.next 
            if current_node == self.head: 
                break

    def reverse_traversal(self): 
        if not self.head: 
            return 
        current_node = self.tail 
        while True: 
            print(current_node.value)
            current_node = current_node.previous 
            if current_node == self.tail: break

    def search(self, value): 
        if not self.head: 
            return None 
        current_node = self.head 
        while True: 
            if current_node.value == value: 
                return True
            current_node = current_node.next 
            if current_node == self.head: 
                break 
        return False

    def get(self, index): 
        if index < 0  or index >= self.length: 
            return None
        if not self.head: 
            return None 
        else: 
            if index < self.length // 2: 
                current_node = self.head 
                for _ in range(index): 
                    current_node = current_node.next 
            else: 
                current_node = self.tail
                for _ in range(self.length-1, index, -1): 
                    current_node = current_node.previous
        return current_node

    def set(self, index, value): 
        target_node = self.get(index)
        if target_node: 
            target_node.value = value
            return True
        return False

    def insert(self, index, value): 
        if index < 0  or index > self.length: 
            return False
        if index == 0: 
            self.prepend(value)
            return True
        if index == self.length: 
            self.append(value)
            return True
        else: 
            new_node = Node(value)
            previous_node = self.get(index-1)
            if previous_node: 
                new_node.previous = previous_node
                new_node.next = previous_node.next 
                previous_node.next.previous = new_node 
                previous_node.next = new_node
            self.length += 1
        return True

    def pop_first(self): 
        if self.length == 0: 
            return None
        removed_node = self.head 
        if self.length == 1: 
            self.head = None
            self.tail = None
        else: 
            self.head = removed_node.next
            self.head.previous = self.tail 
            self.tail.next = self.head  
        removed_node.next = None 
        removed_node.previous = None
        self.length -= 1
        return removed_node

    def pop(self): 
        if self.length == 0: 
            return None
        removed_node = self.tail 
        if self.length == 1: 
            self.head = None
            self.tail = None
        else: 
            self.tail = removed_node.previous
            self.tail.next = self.head 
            self.head.previous = self.tail  
        removed_node.next = None 
        removed_node.previous = None
        self.length -= 1
        return removed_node    

    def remove(self, index): 
        if index < 0 or index >= self.length: 
            return None 
        if index == 0: 
            return self.pop_first() 
        if index == self.length -1: 
            return self.pop()
        removed_node = self.get(index)
        removed_node.previous.next = removed_node.next
        removed_node.next.previous = removed_node.previous
        removed_node.next = None 
        removed_node.previous = None
        self.length -= 1
        return removed_node

    def delete_all(self): 
        if not self.head: 
            return  

        self.head = None 
        self.tail = None 
        self.length = 0

    def __str__(self):
        if self.length == 0: 
            return ""
        current_node = self.head 
        values = []
        while current_node.next is not self.head: 
            values.append(str(current_node.value))
            current_node =  current_node.next 
        values.append(str(current_node.value))
        return " <-> ".join(values) 

cdll = CircularDoubleLinkedList()
cdll.append(10)
cdll.append(20)
cdll.prepend(51)
cdll.append(30)
cdll.append(116)
print(cdll)
# cdll.traverse()
# print(cdll)
# cdll.reverse_traversal()
print(cdll.search(40))
print(cdll.get(4).value)
cdll.set(3, 99)
print(cdll)
cdll.insert(5, 555)
print(cdll)
cdll.pop_first()
print(cdll)
cdll.pop()
print(cdll)
cdll.remove(1)
print(cdll)
