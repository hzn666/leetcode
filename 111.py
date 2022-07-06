from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: TreeNode) -> int:
    if not root:
        return 0

    que = deque([(root, 1)])

    while que:
        size = len(que)

        for _ in range(size):
            cur, dpt = que.popleft()
            if cur.left is None and cur.right is None:
                return dpt
            if cur.left:
                que.append((cur.left, dpt + 1))
            if cur.right:
                que.append((cur.right, dpt + 1))
