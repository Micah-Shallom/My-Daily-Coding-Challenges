class BinaryTree:
    def __init__(self, size) -> None:
        self.maxSize = size
        self.customList = size * [None]
        self.lastUsedIndex = 0

    #inserting a node in the binarytree
    """
    - the binary tree is full
    - we have to look for a first vacant place
    """
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex + 1
        return "The value has been inserted successfully"