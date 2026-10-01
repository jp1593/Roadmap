"""

How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and 
min should all operate in O(1) 


### **Min Stack ($O(1)$ Operations) — Summary**

#### **Core Concept**

To achieve $O(1)$ time complexity for `push`, `pop`, and `get_minimum`, we must avoid searching through the stack when popping the current minimum element. We do this by maintaining a **parallel snapshot of minimum values** as elements are added and removed.

#### **How It Works**

1. **Underlying Structure:** A Singly Linked List handles standard stack behavior (`push` / `pop` at the head/top in $O(1)$).
2. **Min Tracker (`self.min_vals` list):** A standard list that tracks the minimum value at every single step of the stack's history.
3. **`push(val)`**: Compares `val` with the current top of `min_vals` (`min_vals[-1]`):
* If `val` is smaller, append `val` as the new minimum.
* If `val` is larger, append the previous minimum again (creating a historical snapshot).


4. **`pop()`**: Removes the top node from the linked list **and** removes the top element from `min_vals` (`min_vals.pop()`). This automatically rolls back the minimum to what it was *before* that element was added.
5. **`get_minimum()`**: Simply reads `min_vals[-1]` in $O(1)$ time without modifying any state.

### **Key Takeaway**

> *Every push creates a snapshot of the minimum at that point in time. Every pop restores the minimum to its previous snapshot.*
"""

class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None 

class Stack: 
    def __init__(self):
        self.top = None
        self.length = 0
        self.min_vals = []

    def push(self, value): 
        new_node = Node(value)
        if self.length == 0: 
            self.top = new_node
        else:  
            new_node.next = self.top 
            self.top = new_node 
        if len(self.min_vals) == 0: 
            self.min_vals.append(self.top.value)
        elif self.top.value < self.min_vals[-1]: 
            self.min_vals.append(self.top.value)
        else: 
            self.min_vals.append(self.min_vals[-1])
        self.length += 1


    def get_minimum(self): 
        return self.min_vals[-1]

    def pop(self): 
        if self.top is None: 
            return None
        removed_node  = self.top 
        self.top = removed_node.next 
        removed_node.next = None
        self.length -= 1
        self.min_vals.pop()
        return removed_node

    def peek(self): 
        return self.top 

    def isEmpty(self): 
        return self.length == 0

    def clear(self): 
        self.top = None
        self.length = 0
        self.min_vals = []

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
my_stack.push(2)
print("\nMin values:",my_stack.min_vals)
print("\nMinimum value:",my_stack.get_minimum())
print(f"\nComplete list:\n{my_stack}")
my_stack.pop()
print("\nMin values:",my_stack.min_vals)
print("\nMinimum value:",my_stack.get_minimum())