import collections
from typing import Optional, List


class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largestValues(root: Optional[TreeNode]) -> List[int]:
    res = []

    if not root:
        return res

    que = collections.deque([root])

    while que:
        result = []

        for _ in range(len(que)):
            cur = que.popleft()
            result.append(cur.val)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
        res.append(max(result))
    return res