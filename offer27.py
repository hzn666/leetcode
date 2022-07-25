class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mirrorTree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    root.left, root.right = mirrorTree(root.right), mirrorTree(root.left)
    return root