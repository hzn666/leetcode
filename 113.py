import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    res = []

    if not root:
        return res

    stack = collections.deque()
    path = [root.val]
    stack.append((root, path))

    while stack:
        cur, path = stack.popleft()
        if not cur.left and not cur.right and sum(path) == targetSum:
            res.append(path)

        if cur.left:
            stack.append((cur.left, path + [cur.left.val]))
        if cur.right:
            stack.append((cur.right, path + [cur.right.val]))
    return res
