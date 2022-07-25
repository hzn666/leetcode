from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def levelOrder(root: TreeNode) -> List[List[int]]:
    res = []
    even = False

    if not root:
        return res

    queue = deque([root])

    while queue:
        size = len(queue)
        result = []

        for _ in range(size):
            cur = queue.popleft()
            result.append(cur.val)

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        if even:
            res.append(result[::-1])
        else:
            res.append(result)

        even = 1 - even
    return res
