import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root: TreeNode) -> List[List[int]]:
    res = []

    if not root:
        return res

    que = collections.deque([root])

    while que:
        size = len(que)
        result = []

        for _ in range(size):
            cur = que.popleft()
            result.append(cur.val)

            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
        res.append(result)

    return res[::-1]