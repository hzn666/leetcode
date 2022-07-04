from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []

    def traversal(root):
        if root is None:
            return

        traversal(root.left)
        res.append(root.val)
        traversal(root.right)

    traversal(root)
    return res