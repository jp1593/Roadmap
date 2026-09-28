class Stack: 
    def __init__(self):
        self.items = []

    def __str__(self):
        if self.isEmpty(): 
            return "Stack is empty"
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)

    def isEmpty(self): 
        return len(self.items) == 0

    def push(self, element): 
        self.items.append(element)

    def pop(self): 
        if self.isEmpty(): 
            return "Stack is empty"
        return self.items.pop()

    def peek(self): 
        if self.isEmpty(): 
            return "Stack is empty"
        return self.items[-1]

my_stack = Stack()
my_stack.push(100)
my_stack.push(90)
my_stack.push(80)
my_stack.push(70)
print(my_stack, '\n')
print(my_stack.isEmpty(), '\n')
my_stack.pop()
print(my_stack, '\n')
print(my_stack.peek())
