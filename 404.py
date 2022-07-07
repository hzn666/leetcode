from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    cur = 0
    if root.left and not root.left.left and not root.left.right:
        cur = root.left.val

    left = self.sumOfLeftLeaves(root.left)
    right = self.sumOfLeftLeaves(root.right)

    return cur + left + right
