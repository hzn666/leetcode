class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    if not preorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    if len(preorder) == 1:
        return root

    index = inorder.index(root_val)

    inorder_left = inorder[:index]
    inorder_right = inorder[index + 1:]

    preorder_left = preorder[1:len(inorder_left) + 1]
    preorder_right = preorder[len(inorder_left) + 1:]

    root.left = buildTree(preorder_left, inorder_left)
    root.right = buildTree(preorder_right, inorder_right)

    return root