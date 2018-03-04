# DFS

def preorder(root):
    if root != 0:
        yield root.value
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root != 0:
        postorder(root.left)
        postorder(root.right)
        yield root.value


def inorder(root):
    if root != 0:
        inorder(root.left)
        yield root.value
        inorder(root.right)
