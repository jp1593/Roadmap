# List Queue - With Fixed Capacity

class Queue: 
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1 
        self.top = -1 

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self): 
        if self.top + 1 == self.start: 
            return True 
        elif self.start == 0 and self.top + 1 == self.maxSize: 
            return True
        else: 
            return False

    def isEmpty(self): 
        return self.top == -1

    def enqueue(self, value): 
        if self.isFull(): 
            return "The Queue has reached it's max capacity"
        else: 
            if self.top + 1 == self.maxSize: 
                self.top = 0 
            else: 
                self.top += 1
                if self.start == -1: 
                    self.start = 0
            self.items[self.top] = value
            return "Element inserted at the end of the Queue"

    def deque(self): 
        if self.isEmpty(): 
            return "The Queue doesn't have any element on it"
        else: 
            firstElement = self.items[self.start]
            start = self.start 
            if self.start == self.top: 
                self.start = -1 
                self.top =-1 
            elif self.start + 1 == self.maxSize: 
                self.start = 0
            else: 
                self.start += 1
            self.items[start] = None 
            return firstElement

my_queue = Queue(5)
print(my_queue)
print(my_queue.isFull())
print(my_queue.isEmpty())
my_queue.enqueue(12)
my_queue.enqueue(24)
my_queue.enqueue(32)
print(my_queue)
my_queue.deque()
my_queue.deque()
print(my_queue)
my_queue.enqueue(100)
my_queue.enqueue(200)
my_queue.enqueue(300)
print(my_queue)