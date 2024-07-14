from Queue import Queue
class TreeNode:
    def __init__(self, value) -> None:
        self.data = value
        self.leftChild = None
        self.rightChild = None

newTree = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
cola =  TreeNode("Cola")
fanta = TreeNode("Fanta")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild.leftChild = cola
rightChild.rightChild = fanta
newTree.leftChild = leftChild
newTree.rightChild = rightChild


def searchBT(rootNode: object, nodeValue: str) -> str:
    if rootNode is None:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            rootNode = customQueue.dequeue()
            if rootNode.value.data == nodeValue:
                print("Success")
                return 
            if (rootNode.value.leftChild is not None):
                customQueue.enqueue(rootNode.value.leftChild)
            if (rootNode.value.rightChild is not None):
                customQueue.enqueue(rootNode.value.rightChild)
        print("Not Found")
        return 
    
searchBT(newTree, "Tea")