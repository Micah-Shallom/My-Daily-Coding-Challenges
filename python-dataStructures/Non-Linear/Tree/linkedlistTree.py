class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None


newTree = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newTree.leftChild = leftChild
newTree.rightChild = rightChild

def preOrderTraversal(RootNode):
    if not RootNode:
        return
    print(RootNode.data)
    preOrderTraversal(RootNode.leftChild)
    preOrderTraversal(RootNode.rightChild)

def inOrderTraversal(RootNode):
    if not RootNode:
        return
    inOrderTraversal(RootNode.leftChild)
    print(RootNode.data)
    inOrderTraversal(RootNode.rightChild)

def postOrderTraversal(RootNode):
    if not RootNode:
        return
    postOrderTraversal(RootNode.leftChild)
    postOrderTraversal(RootNode.rightChild)
    print(RootNode.data)

preOrderTraversal(newTree)
inOrderTraversal(newTree)