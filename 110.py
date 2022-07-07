class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: TreeNode) -> bool:
    def recur(root):
        if not root:
            return 0
        left = recur(root.left)
        if left == -1:
            return -1
        right = recur(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

    return recur(root) != -1


# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         if not root: return True
#         return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
#             self.isBalanced(root.left) and self.isBalanced(root.right)
#
#     def depth(self, root):
#         if not root: return 0
#         return max(self.depth(root.left), self.depth(root.right)) + 1
