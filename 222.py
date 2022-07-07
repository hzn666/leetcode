from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root: TreeNode) -> int:
    num = 0
    if not root:
        return num

    que = deque([root])
    num += 1

    while que:
        size = len(que)

        for _ in range(size):
            cur = que.popleft()
            if cur.left:
                num += 1
                que.append(cur.left)
            if cur.right:
                num += 1
                que.append(cur.right)
    return num
