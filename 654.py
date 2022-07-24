class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums):
    if not nums:
        return None

    maxValue = max(nums)
    index = nums.index(maxValue)

    root = TreeNode(maxValue)

    left = nums[:index]
    right = nums[index+1:]

    root.left = constructMaximumBinaryTree(left)
    root.right = constructMaximumBinaryTree(right)

    return root
