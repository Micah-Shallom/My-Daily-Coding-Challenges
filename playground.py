from play2 import Queue

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

rootTree = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
rootTree.leftChild = hot
rootTree.rightChild = cold
tea = TreeNode("Tea")
coffee =TreeNode("Coffee")
fanta = TreeNode("Fanta")
cola = TreeNode("Cola")
rootTree.leftChild.leftChild = tea
rootTree.leftChild.rightChild = coffee
rootTree.rightChild.leftChild = cola
rootTree.rightChild.rightChild = fanta

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            rootNode = customQueue.dequeue()
            print(rootNode.value.data)
            if(rootNode.value.leftChild is not None):
                customQueue.enqueue(rootNode.value.leftChild)
            if(rootNode.value.rightChild is not None):
                customQueue.enqueue(rootNode.value.rightChild)

levelOrderTraversal(rootTree)