class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

# Method to add a node at the end of the list
    def append(self, value): 
        new_node = Node(value)
        if self.length == 0 : 
            self.head = new_node 
            self.tail = new_node
            new_node.next = new_node 
        else: 
            self.tail.next = new_node 
            self.tail = new_node 
            new_node.next = self.head
        self.length += 1

# Method to add a node at the beggining of the list
    def prepend(self, value): 
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node 
            new_node.next = new_node
        else: 
            new_node.next = self.head 
            self.head = new_node 
            self.tail.next = new_node
        self.length += 1

# Method to insert a node at somepoint in the list
    def insert(self, value, index): 
        if index > self.length or index < 0: 
            raise Exception("Index out of range")

        if index == 0: 
            return self.prepend(value)

        if index == self.length: 
            return self.append(value)

        new_node = Node(value)
        prev_node = self.head 
        for _ in range(index-1): 
            prev_node = prev_node.next 
        new_node.next = prev_node.next 
        prev_node.next = new_node
        self.length += 1

# Method to loop the list and get each node
    def traverse(self): 
        current = self.head 
        while current: 
            print(current.value)
            current = current.next 
            if current == self.head: 
                break

# Method to check if the target value is in a node inside the list
    def search(self, target): 
        current = self.head 
        while current: 
            if current.value == target: 
                return True
            current = current.next 
            if current == self.head: 
                break
        return False

# Method to get a node by the index 
    def get(self, index): 
        current = self.head 
        if index >= self.length or index < 0: 
            raise Exception("Invalid index")
        for _ in range(index): 
            current = current.next 
        return current

# Method to change the value of a node in a specific index 
    def set(self, index, value): 
        if index >= self.length or index < 0:
            raise Exception("Invalid index")
        target_node = self.get(index)  # Handles bounds check and traversal
        target_node.value = value

# Method that erases the first node of the list
    def pop_first(self): 
        pop_node = self.head 
        if self.length == 0: 
            return None
        if self.length == 1: 
            self.head = None
            self.tail = None
            self.length -= 1
            return pop_node
        else: 
            self.head = pop_node.next 
            pop_node.next = None 
            self.tail.next = self.head 
            self.length -= 1
        return pop_node 

# Method that erase the last node of the list, returing the removed node
    def pop(self): 
        if self.length == 0: 
            return None
        if self.length == 1: 
            popped_node = self.head 
            self.head = None 
            self.tail = None
            self.length -= 1
            popped_node.next = None
            return popped_node
        else: 
            previous_node = self.head
            for _ in range(self.length-2): 
                previous_node = previous_node.next 
            popped_node = self.tail
            self.tail = previous_node 
            self.tail.next = self.head 
            popped_node.next = None
            self.length -= 1
            return popped_node

# Method to remove a node from the list based on the index 
    def remove(self, index): 
        if index < 0 or index >= self.length:
             raise Exception("Index out of range")
        if index == 0: 
            return self.pop_first()
        if index == (self.length-1): 
            return self.pop() 
        remove_node = self.get(index)
        previous_node = self.get(index-1)
        previous_node.next = remove_node.next 
        remove_node.next = None
        self.length -= 1
        return remove_node 

# Method to delete all the nodes of the linked list
    def delete_all(self): 
        if self.length == 0: 
            return None
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0



# Method to print the node values of the whole list
    def __str__(self):
        temp_node = self.head 
        result = ''
        while temp_node is not None:  
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head: 
                break  
            result += ' -> '
        return result
    
cslinkedlist = CSLinkedList()
cslinkedlist.append(1)
cslinkedlist.append(2)
cslinkedlist.append(3)
print(cslinkedlist)
cslinkedlist.prepend(20)
print(cslinkedlist)
cslinkedlist.insert(100, 4)
print(cslinkedlist)
# cslinkedlist.traverse()
print(cslinkedlist.search(20))
print(cslinkedlist.get(4).value)
cslinkedlist.set(4, 222)
print(cslinkedlist)
cslinkedlist.pop_first() 
print(cslinkedlist)
cslinkedlist.pop()
print("Before remove:", cslinkedlist)
print("Removed node:", cslinkedlist.remove(2).value)
print(cslinkedlist)
cslinkedlist.delete_all()
print(cslinkedlist)