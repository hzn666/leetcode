class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    st = [root]
    while st:
        node = st.pop()
        node.left, node.right = node.right, node.left
        if node.right:
            st.append(node.right)
        if node.left:
            st.append(node.left)
    return root
