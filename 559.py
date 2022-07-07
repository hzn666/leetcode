from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def maxDepth(root: 'Node') -> int:
    depth = 0
    if not root:
        return depth

    que = deque([root])

    while que:
        size = len(que)
        depth += 1

        for _ in range(size):
            cur = que.popleft()
            if cur.children:
                que.extend(cur.children)

    return depth
