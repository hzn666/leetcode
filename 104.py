import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(self, root: Optional[TreeNode]) -> int:
    depth = 0
    if not root:
        return depth

    que = collections.deque([root])

    while que:
        depth += 1

        for _ in range(len(que)):
            cur = que.popleft()
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)

    return depth
