import sys
import os

# This part is required to set the path for the usage of the custom Queue created time before
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Queue.LinkedList_Queue as queue

class TreeNode: 
    def __init__(self, data):
        self.rightChild = None 
        self.leftChild = None
        self.data = data

newBT = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
hot.leftChild = tea 
hot.rightChild = coffee
newBT.leftChild = hot 
newBT.rightChild = cold

def preOrderTraversal(rootNode): 
    if not rootNode: 
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

print("--- Pre-Order ---")
preOrderTraversal(newBT)
print()

def inOrderTraversal(rootNode): 
    if not rootNode: 
        return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

print("--- In-Order ---")
inOrderTraversal(newBT)
print()

def postOrderTraversal(rootNode): 
    if not rootNode: 
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

print("--- Post-Order ---")
postOrderTraversal(newBT)
print()


def levelOrderTraversal(rootNode):  
    if not rootNode: 
        return 
    else: 
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty(): 
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None: 
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None: 
                customQueue.enqueue(root.value.rightChild)

 
print("--- Level-Order ---")
levelOrderTraversal(newBT)
print()