class BSTNode:
    def __init__(self,data):
        self.data = data
        self.LeftChild = None
        self.RightChild = None
        
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.LeftChild is None:
            rootNode.LeftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.LeftChild, nodeValue)
    else:
        if rootNode.RightChild is None:
            rootNode.RightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.RightChild, nodeValue)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data , end=" ")
    preOrderTraversal(rootNode.LeftChild)
    preOrderTraversal(rootNode.RightChild)
    
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.LeftChild)
    print(rootNode.data, end=" ")
    inOrderTraversal(rootNode.RightChild)
    
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.LeftChild)
    postOrderTraversal(rootNode.RightChild)
    print(rootNode.data, end=" ")
        
newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
# preOrderTraversal(newBST)
inOrderTraversal(newBST)
# postOrderTraversal(newBST)
