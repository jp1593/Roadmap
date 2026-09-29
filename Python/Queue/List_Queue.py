class Queue: 
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self): 
        return len(self.items) == 0

    def enqueue(self, value): 
        self.items.append(value)

my_queue = Queue()
print(my_queue.isEmpty())
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
print(my_queue)