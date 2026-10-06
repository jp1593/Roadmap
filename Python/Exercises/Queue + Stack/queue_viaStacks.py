"""
Implement Queue class which implements a queue using two stacks
"""

class Stack(): 
    def __init__(self):
        self.list = []

    def __len__(self): 
        return len(self.list)

    def push(self, value): 
        self.list.append(value)

    def pop(self): 
        if len(self.list) == 0: 
            return None
        return self.list.pop()

class QueueViaStack(): 
    def __init__(self):
        self.inStack = Stack() 
        self.outStack = Stack()

    def enqueue(self, value): 
        self.inStack.push(value)

    def dequeue(self): 
        while len(self.inStack): 
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack): 
            self.inStack.push(self.outStack.pop())
        return result

# --- Test Execution ---
q = QueueViaStack()

print("1. Enqueueing elements 10, 20, 30...")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(f"Dequeue: {q.dequeue()}")  # Expected: 10
print(f"Dequeue: {q.dequeue()}")  # Expected: 20

print("\n2. Enqueueing element 40...")
q.enqueue(40)

print(f"Dequeue: {q.dequeue()}")  # Expected: 30
print(f"Dequeue: {q.dequeue()}")  # Expected: 40
print(f"Dequeue on empty queue: {q.dequeue()}")  # Expected: None