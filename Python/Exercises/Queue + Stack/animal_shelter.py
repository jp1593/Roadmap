"""
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" 
basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they
can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). 

They cannot select which specific animal they would like. Create the data structures to maintain this system and implement
operations such as enqueue, dequeAny, dequeueDog, and dequeueCat. 
"""

class Node: 
    def __init__(self, animal_type, order):
        self.animal_type = animal_type
        self.order = order
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None 
        self.tail = None 

    def append(self, animal_type, order): 
        new_node = Node(animal_type, order)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node 
            self.tail = new_node 

    def popfirst(self): 
        if self.head is None: 
            return None
        
        removed_node = self.head 
        self.head = self.head.next
        
        if self.head is None:  
            self.tail = None
            
        removed_node.next = None
        return removed_node

    def peek(self): 
        return self.head

class AnimalShelter(): 
    def __init__(self):
        self.dogs_list = LinkedList()
        self.cats_list = LinkedList()
        self.order = 0 

    def enqueue(self, animal_type): 
        if animal_type == "Dogs": 
            self.order += 1
            self.dogs_list.append(animal_type, self.order)
        elif animal_type == "Cats": 
            self.order += 1
            self.cats_list.append(animal_type, self.order)
        else: 
            return "Animal Shelter don't allow that animal"

    def dequeDog(self): 
        return self.dogs_list.popfirst()

    def dequeCat(self): 
        return self.cats_list.popfirst()

    def dequeAny(self): 
        if self.dogs_list.head is None and self.cats_list.head is None: 
            return "Animal Shelter don't have any dogs or cats on adoption"

        if self.dogs_list.head is None:
            return self.cats_list.popfirst()
        
        if self.cats_list.head is None:
            return self.dogs_list.popfirst()
        
        if self.dogs_list.peek().order < self.cats_list.peek().order:
            return self.dogs_list.popfirst()
        else:
            return self.cats_list.popfirst()
            
# Helper function to print node details
def print_adopted(node):
    if isinstance(node, Node):
        print(f"Adopted: {node.animal_type} (Arrival Order: {node.order})")
    else:
        print(node)

shelter = AnimalShelter()

# 1. Enqueue animals in alternating order
shelter.enqueue("Dogs")  # Order: 1
shelter.enqueue("Cats")  # Order: 2
shelter.enqueue("Cats")  # Order: 3
shelter.enqueue("Dogs")  # Order: 4
shelter.enqueue("Dogs")  # Order: 5

# 2. Test dequeueAny (Should return Dog with order 1)
print_adopted(shelter.dequeAny()) 

# 3. Test dequeueDog (Should return Dog with order 4)
print_adopted(shelter.dequeDog()) 

# 4. Test dequeueAny (Should return Cat with order 2 over Dog with order 5)
print_adopted(shelter.dequeAny()) 

# 5. Test dequeueAny (Should return Cat with order 3 over Dog with order 5)
print_adopted(shelter.dequeAny()) 

# 6. Test dequeueAny with only Dogs left (Should return Dog with order 5)
print_adopted(shelter.dequeAny()) 

# 7. Test empty shelter edge case
print_adopted(shelter.dequeAny())