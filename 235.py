class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    return root