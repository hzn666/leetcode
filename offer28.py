class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root):
    def compare(left, right):
        if not left and right:
            return False
        if left and not right:
            return False
        if not left and not right:
            return True
        if left.val != right.val:
            return False

        return compare(left.left, right.right) and compare(left.right, right.left)

    if not root:
        return True
    return compare(root.left, root.right)