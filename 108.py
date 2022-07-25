from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(nums, left, right):
    if left > right:
        return None

    mid = left + (right - left) // 2
    root = TreeNode(nums[mid])
    root.left = helper(nums, left, mid - 1)
    root.right = helper(nums, mid + 1, right)
    return root


def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    root = helper(nums, 0, len(nums) - 1)
    return root
