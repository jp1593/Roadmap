class Stack: 
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)

    def push(self, element): 
        self.items.append(element)

my_stack = Stack()
my_stack.push(100)
my_stack.push(90)
my_stack.push(80)
my_stack.push(70)
print(my_stack)
