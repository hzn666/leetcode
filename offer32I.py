from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(self, root: TreeNode) -> List[int]:
    res = []
    if not root:
        return res

    queue = deque([root])

    while queue:
        cur = queue.popleft()
        res.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)

    return res
