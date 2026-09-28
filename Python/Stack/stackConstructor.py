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

my_stack = Stack()
my_stack.push(100)
my_stack.push(90)
my_stack.push(80)
my_stack.push(70)
print(my_stack)
print(my_stack.isEmpty())
