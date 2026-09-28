class Stack: 
    def __init__(self):
        self.items = []

    def push(self, element): 
        self.items.append(element)

my_stack = Stack()
my_stack.push(100)
my_stack.push(90)
my_stack.push(80)
my_stack.push(70)
print(my_stack.items)
