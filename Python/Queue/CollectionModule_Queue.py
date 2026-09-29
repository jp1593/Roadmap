# collections.deque as a Fifo queue: 
from collections import deque 

customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4) #Notice that adding this makes the first element to go out of the Queue, bc it exceedes the max_len 
print(customQueue)
print(customQueue.popleft())
print(customQueue)
customQueue.clear()
print(customQueue)