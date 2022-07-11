from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode:
    if not postorder:
        return None

    root_val = postorder[-1]
    root = TreeNode(root_val)

    if len(postorder) == 1:
        return root

    index = inorder.index(root_val)

    inorder_left = inorder[:index]
    inorder_right = inorder[index + 1:]

    postorder_left = postorder[:len(inorder_left)]
    postorder_right = postorder[len(inorder_left):-1]

    root.left = buildTree(inorder_left, postorder_left)
    root.right = buildTree(inorder_right, postorder_right)

    return root
