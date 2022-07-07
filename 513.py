from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findBottomLeftValue(root: Optional[TreeNode]) -> int:
    que = deque([root])
    res = 0

    while que:
        size = len(que)
        res = que[0].val
        for _ in range(size):
            cur = que.popleft()

            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
    return res
