from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    result = []

    def traversal(root):
        if root is None:
            return

        traversal(root.left)
        result.append(root.val)
        traversal(root.right)

    traversal(root)

    for i in range(1, len(result)):
        if result[i - 1] >= result[i]:
            return False

    return True
