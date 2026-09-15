# Creating tree
class Node:
    def __init__ (self, value):
        self.value=value
        self.left=None
        self.right=None
def inorder(root):
    if root is None:
        return
    
    inorder(root.left)     # Recursive call on left
    print(root.value, end=" ") 
    inorder(root.right)      # Recursive call on right
def preorder(root):
    if root is None:
        return
    
    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.value, end=" ")           
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)