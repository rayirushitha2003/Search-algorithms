
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)
root = Node("CEO")

root.left = Node("Manager A")
root.right = Node("Manager B")

root.left.left = Node("Team Lead 1")
root.left.right = Node("Team Lead 2")

root.left.left.left = Node("Employee X")

print("Company Levels (Height):", height(root))