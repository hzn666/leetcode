class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubStructure(A: TreeNode, B: TreeNode) -> bool:
    def recur(A, B):
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return recur(A.left, B.left) and recur(A.right, B.right)

    if not A or not B:
        return False
    return recur(A, B) or isSubStructure(A.left, B) or isSubStructure(A.right, B)