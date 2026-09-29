# List Queue - With Fixed Capacity

class Queue: 
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1 
        self.top = -1 


my_queue = Queue(5)