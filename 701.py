class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    # 返回更新后的以当前root为根节点的新树，方便用于更新上一层的父子节点关系链

    # Base Case
    if not root: return TreeNode(val)

    # 单层递归逻辑:
    if val < root.val:
        # 将val插入至当前root的左子树中合适的位置
        # 并更新当前root的左子树为包含目标val的新左子树
        root.left = insertIntoBST(root.left, val)

    if root.val < val:
        # 将val插入至当前root的右子树中合适的位置
        # 并更新当前root的右子树为包含目标val的新右子树
        root.right = insertIntoBST(root.right, val)

    # 返回更新后的以当前root为根节点的新树
    return root
