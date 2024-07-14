from Queue import Queue

class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
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

def levelOrderTraversal(RootNode):
    if not RootNode:
        return
    else:
        queue = Queue()
        queue.enqueue(RootNode)
        while not(queue.isEmpty()):
            root = queue.dequeue()
            print(root.value.data)

            if root.value.leftChild is not None:
                queue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                queue.enqueue(root.value.rightChild)


def searchBT(rootNode, nodeValue):
    if rootNode is None:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)





print(searchBT(newTree, "Tea"))

# levelOrderTraversal(newTree)
        



# preOrderTraversal(newTree)
# inOrderTraversal(newTree)