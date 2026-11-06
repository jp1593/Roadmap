class TreeNode: 
    def __init__(self, data):
        self.rightChild = None 
        self.leftChild = None
        self.data = data

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild 
newBT.rightChild = rightChild

def preOrderTraversal(rootNode): 
    if not rootNode: 
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

preOrderTraversal(newBT)

