class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMode(root):
    stack = []
    cur = root
    pre = None
    maxCount = 0
    count = 0

    res = []

    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if not pre:
                count = 1
            elif cur.val == pre.val:
                count += 1
            else:
                count = 1

            if count == maxCount:
                res.append(cur.val)
            if count > maxCount:
                res = [cur.val]

            pre = cur
            cur = cur.right

        return res
