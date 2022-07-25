from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == key:
        if not root.left and not root.right:
            del root
            return None
        if not root.left and root.right:
            tmp = root
            root = root.right
            del tmp
            return root
        if not root.right and root.left:
            tmp = root
            root = root.left
            del tmp
            return root
        else:
            v = root.right
            while v.left:
                v = v.left
            v.left = root.left
            tmp = root
            root = root.right
            del tmp
            return root

    if root.val > key:
        root.left = deleteNode(root.left, key)
    if root.val < key:
        root.right = deleteNode(root.right, key)
    return root
