# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        if not root:
            return "[]"

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")

        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return
        vals = data[1:-1].split(",")
        i = 1

        root = TreeNode(vals[0])
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))