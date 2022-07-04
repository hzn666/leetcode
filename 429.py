import collections
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root: 'Node') -> List[List[int]]:
    res = []

    if not root:
        return res

    que = collections.deque([root])

    while que:
        result = []

        for _ in range(len(que)):
            cur = que.popleft()
            result.append(cur.val)

            if cur.children:
                que.extend(cur.children)
        res.append(result)

    return res

