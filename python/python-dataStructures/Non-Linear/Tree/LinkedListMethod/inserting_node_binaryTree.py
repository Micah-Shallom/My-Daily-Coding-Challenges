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
# cola =  TreeNode("Cola")
fanta = TreeNode("Fanta")
leftChild.leftChild = tea
leftChild.rightChild = coffee
# rightChild.leftChild = cola
rightChild.rightChild = fanta
newTree.leftChild = leftChild
newTree.rightChild = rightChild

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            rootNode = customQueue.dequeue()
            print(rootNode.value.data)
            if rootNode.value.leftChild is not None:
                customQueue.enqueue(rootNode.value.leftChild)
            if rootNode.value.rightChild is not None:
                customQueue.enqueue(rootNode.value.rightChild)


def insertBT(rootNode, newNode):
    if not rootNode :
        rootNode = newNode
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            rootNode = customQueue.dequeue()
            if rootNode.value.leftChild is not None:
                customQueue.enqueue(rootNode.value.leftChild)
            else:
                rootNode.value.leftChild = newNode
                return f"Successfully added to leftNode of {rootNode.value.data}"
            if rootNode.value.rightChild is not None:
                customQueue.enqueue(rootNode.value.rightChild)
            else:
                rootNode.value.rightChild = newNode
                return f"Successfully added to rightNode of {rootNode.value.data}"

# newNode = TreeNode("Cola")
# print(insertBT(newTree, newNode))
# levelOrderTraversal(newTree)