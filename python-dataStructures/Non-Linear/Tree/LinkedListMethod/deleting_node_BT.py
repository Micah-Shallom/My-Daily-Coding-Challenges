from Queue import Queue
from inserting_node_binaryTree import levelOrderTraversal
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

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            rootNode = customQueue.dequeue()
            if rootNode.value.leftChild is not None:
                customQueue.enqueue(rootNode.value.leftChild)
            # else:
            #     deepestNode = rootNode.value
            if rootNode.value.rightChild is not None:
                customQueue.enqueue(rootNode.value.rightChild)
            # else:
            #     deepestNode = rootNode.value
        deepestNode = rootNode.value
        return deepestNode
    
def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            rootNode = customQueue.dequeue()
            if rootNode is deepestNode:
                rootNode.value = None
                return
            if rootNode.value.rightChild:
                if rootNode.value.rightChild is deepestNode:
                    rootNode.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(rootNode.value.rightChild)
                    
            if rootNode.value.leftChild:
                if rootNode.value.leftChild is deepestNode:
                    rootNode.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(rootNode.value.leftChild)

dNode = getDeepestNode(newTree)
deleteDeepestNode(newTree, dNode)
levelOrderTraversal(newTree)
