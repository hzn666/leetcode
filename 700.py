class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: TreeNode, val: int) -> TreeNode:
    if root == None or root.val == val:
        return root

    if root.val < val:
        return searchBST(root.right, val)
    if root.val > val:
        return searchBST(root.left, val)
