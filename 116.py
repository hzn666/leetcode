import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return

    que = collections.deque([root])

    while que:
        size = len(que)
        for _ in range(size):
            cur = que.popleft()

            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
            if _ == size - 1:
                break
            cur.next = que[0]
    return root