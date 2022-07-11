from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    def isornot(root, targetSum):
        if not root.left and not root.right and targetSum == 0:
            return True
        if not root.left and not root.right:
            return False

        if root.left:
            targetSum -= root.left.val
            if isornot(root.left, targetSum):
                return True
            targetSum += root.left.val
        if root.right:
            targetSum -= root.right.val
            if isornot(root.right, targetSum):
                return True
            targetSum += root.right.val
        return False

    if not root:
        return False
    else:
        return isornot(root, targetSum - root.val)


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    stack = []
    stack.append((root, root.val))

    while stack:
        cur, path = stack.pop()

        if not cur.left and not cur.right and path == targetSum:
            return True
        if cur.left:
            stack.append((cur.left, path + cur.left.val))
        if cur.right:
            stack.append((cur.right, path + cur.right.val))
    return False
