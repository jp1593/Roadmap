""" 
Imagine a (literal stack of plates). If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack 
when the previous stack exceeds the treshold. Implement a data strcuture SetOfStacks that mimics this. SetOfStacks should be composed of several stacks 
and should create a new stack once the previous one exceeds capacity, SetofStacks.push() and SetofStacks.pop() should behave identically to a single 
stack (that is, pop() should return the same values as it would if there were just a single stack). 

Follow Up: Implement a function popAt (int index) which performs a pop operation on a specific sub - stack

"""

class Stack: 
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def __str__(self):
        if self.isEmpty(): 
            return "Stack is empty"
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)

    def isEmpty(self): 
        return len(self.items) == 0

    def isFull(self): 
        return len(self.items) == self.capacity

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

    def size(self): 
        return len(self.items)

    def clear(self): 
        self.items = []

    def removeBottom(self):
        if not self.isEmpty():
            return self.items.pop(0)

class SetOfStacks: 
    def __init__(self, stackSize):
        self.stackSize = stackSize
        self.stacks = []

    def push(self, value): 
        if len(self.stacks) == 0 or self.stacks[-1].isFull(): 
            new_stack = Stack(self.stackSize)
            new_stack.push(value)
            self.stacks.append(new_stack)
        else: 
            self.stacks[-1].push(value)

    def pop(self): 
        if len(self.stacks) == 0: 
            return "No existance of pile of plates"
        else: 
            eliminated_value = self.stacks[-1].pop()
            if self.stacks[-1].isEmpty(): 
                self.stacks.pop()
            return eliminated_value

    def popAtIndex(self, index):
        if index < 0 or index >= len(self.stacks): 
            return "There isn't a pile on that index"
        else: 
            removed_value = self.stacks[index].pop()
            for i in range(index, len(self.stacks)-1): 
                moved_item = self.stacks[i + 1].removeBottom()
                self.stacks[i].push(moved_item)
            if self.stacks[-1].isEmpty():
                self.stacks.pop()
            return removed_value



def display_set_of_stacks(set_of_stacks):
    """Prints the internal state of all sub-stacks."""
    print(f"\nTotal Sub-Stacks: {len(set_of_stacks.stacks)}")
    for i, stack in enumerate(set_of_stacks.stacks):
        print(f"  Sub-Stack {i} (items bottom -> top): {stack.items}")

# Testing Execution
# ==========================================

# 1. Initialize SetOfStacks with capacity 3 per stack
plate_set = SetOfStacks(stackSize=3)
print("\n--- Initializing SetOfStacks (capacity = 3) ---")
display_set_of_stacks(plate_set)

# 2. Test Pushing 7 Items (Should spill across 3 sub-stacks: [3 items], [3 items], [1 item])
print("\n--- Pushing items 10 through 70 ---")
for val in [10, 20, 30, 40, 50, 60, 70]:
    plate_set.push(val)

display_set_of_stacks(plate_set)

# 3. Test Popping Items
print("\n--- Popping 2 items ---")
print("Popped:", plate_set.pop())  # Expected: 70 (This should empty and delete Sub-Stack 2)
print("Popped:", plate_set.pop())  # Expected: 60 (Popping from Sub-Stack 1)

display_set_of_stacks(plate_set)

# 4. Test popAtIndex (Rollover)
print("\n--- Popping at Index 0 (Sub-Stack 0) ---")
# Currently Sub-Stack 0 is [10, 20, 30] and Sub-Stack 1 is [40, 50]
print("Popped at Index 0:", plate_set.popAtIndex(0)) # Expected: 30
# Rollover should shift 40 (bottom of Sub-Stack 1) into Sub-Stack 0!
# Result should be: Sub-Stack 0: [10, 20, 40], Sub-Stack 1: [50]

display_set_of_stacks(plate_set)

