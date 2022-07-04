import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    res = []

    if not root:
        return res

    que = collections.deque([root])

    while que:
        size = len(que)
        result = 0

        for _ in range(size):
            cur = que.popleft()
            result += cur.val
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)

        res.append(result / size)

    return res