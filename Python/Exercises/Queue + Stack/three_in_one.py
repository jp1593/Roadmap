"""

Describe how you could use a single Python list to implement three stacks

Description:
1. Fixed Division (Memory Layout)
Allocate a single 1D list of size `3 * stackSize`. Divide it into three equal side-by-side blocks:

Stack 0: Indices `0` to `stackSize - 1`
Stack 1: Indices `stackSize` to `2 * stackSize - 1`
Stack 2: Indices `2 * stackSize` to `3 * stackSize - 1`

2. Tracking Size (`self.size`)
Use an array `[0, 0, 0]` where `size[i]` tracks the item count in Stack `i`.

3. Finding the Top Index (The Offset Formula)

| Operation | Formula / Condition |
| --- | --- |
| **Start Index** | `stackNumber * stackSize` |
| **Top Index** | `(stackNumber * stackSize) + size[stackNumber] - 1` |
| **Is Full?** | `size[stackNumber] == stackSize` |
| **Is Empty?** | `size[stackNumber] == 0` |
"""

class MultiStack: 
    def __init__(self, stackSize):
        self.numberStacks = 3 
        self.custList = [0] * (stackSize * self.numberStacks)
        self.size = [0] * self.numberStacks
        self.stackSize = stackSize

    def isFull(self, stackNumber): 
        return self.size[stackNumber] == self.stackSize

    def isEmpty(self, stackNumber): 
        return self.size[stackNumber] == 0

    def indexOfTop(self, stackNumber): 
        offset = stackNumber * self.stackSize
        return offset + self.size[stackNumber] - 1

    def push(self, value, stackNumber): 
        if self.isFull(stackNumber): 
            return "The stack is full"
        else: 
            self.size[stackNumber] += 1
            self.custList[self.indexOfTop(stackNumber)] = value

    def pop(self, stackNumber): 
        if self.isEmpty(stackNumber): 
            return "The stack is empty"
        else: 
            value = self.custList[self.indexOfTop(stackNumber)]
            self.custList[self.indexOfTop(stackNumber)] = 0
            self.size[stackNumber] -= 1
            return value

    def peek(self, stackNumber): 
        if self.isEmpty(stackNumber): 
            return "The stack is empty"
        else: 
            value = self.custList[self.indexOfTop(stackNumber)]
            return value


customStack = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1, 0)
customStack.push(2,0)
customStack.push(3, 2)
print("\nInternal sizes counter:", customStack.size)
print("\nUnderlying custList Array:")
print(customStack.custList)