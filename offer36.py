class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeToDoublyList(root: 'Node') -> 'Node':
    stack = []
    if not root:
        return
    pre = None
    head = None
    cur = root

    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if not pre:
                head = cur
            if pre:
                pre.right = cur
                cur.left = pre
            pre = cur
            cur = cur.right
    pre.right = head
    head.left = pre
    return head


# def dfs(cur):
#     if not cur:
#         return
#     dfs(cur.left)
#     if self.pre:
#         self.pre.right, cur.left = cur, self.pre
#     else:
#         self.head = cur
#     self.pre = cur
#     dfs(cur.right)
#
#
# if not root:
#     return
# self.pre = None
# dfs(root)
# self.head.left, self.pre.right = self.pre, self.head
# return self.head