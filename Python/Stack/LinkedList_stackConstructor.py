class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None 

class Stack: 
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, value): 
        new_node = Node(value)
        if self.length == 0: 
            self.top = new_node
        else:  
            new_node.next = self.top 
            self.top = new_node 
        self.length += 1

    def pop(self): 
        if self.top is None: 
            return None
        removed_node  = self.top 
        self.top = removed_node.next 
        removed_node.next = None
        self.length -= 1
        return removed_node

    def __str__(self):
        values = []
        temp = self.top
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return "\n".join(values)

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print(my_stack, '\n')
my_stack.pop()
print(f"{my_stack}\n\nTop Value: {my_stack.top.value}")