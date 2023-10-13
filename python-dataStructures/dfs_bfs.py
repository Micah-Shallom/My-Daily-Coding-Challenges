class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Function to perform Depth-First Search (DFS) to search for an element in the tree.
def dfs_search(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    # Recursively search in the left and right subtrees.
    return dfs_search(root.left, target) or dfs_search(root.right, target)

# Function to perform Breadth-First Search (BFS) to search for an element in the tree.
def bfs_search(root, target):
    if root is None:
        return False
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        if node.val == target:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False

# Creating a simple binary tree.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Element to search for.
element_to_find = 5

# Perform DFS search.
if dfs_search(root, element_to_find):
    print(f"Element {element_to_find} found using DFS.")
else:
    print(f"Element {element_to_find} not found using DFS.")

# Perform BFS search.
if bfs_search(root, element_to_find):
    print(f"Element {element_to_find} found using BFS.")
else:
    print(f"Element {element_to_find} not found using BFS.")
