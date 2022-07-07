from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    que = deque([p, q])

    while que:
        size = int(len(que) / 2)

        for _ in range(size):
            left = que.popleft()
            right = que.popleft()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            que.append(left.left)
            que.append(right.left)
            que.append(left.right)
            que.append(right.right)

    return True


# if not p and not q:
#     return True
# if not p or not q or p.val != q.val:
#     return False
#
# return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
