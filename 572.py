class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSametree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    return isSametree(p.left, q.left) and isSametree(p.right, q.right)


def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if root:
        return isSametree(root, subRoot) or isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
    return False
