class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinimumDifference(root):
    stack = []
    cur = root
    pre = None

    result = float("inf")

    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if pre:
                result = min(result, cur.val-pre.val)
            pre = cur
            cur = cur.right

    return result
