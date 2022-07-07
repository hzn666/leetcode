from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    path = ""
    result = []
    if not root:
        return result
    self.traversal(root, path, result)
    return result


def traversal(self, cur, path, result):
    path += str(cur.val)
    if not cur.left and not cur.right:
        result.append(path)

    if cur.left:
        self.traversal(cur.left, path + "->", result)
    if cur.right:
        self.traversal(cur.right, path + "->", result)

# stack, path_st, result = deque([root]), deque(), []
# path_st.append(str(root.val))
#
# while stack:
#     cur = stack.pop()
#     path = path_st.pop()
#     # 如果当前节点为叶子节点，添加路径到结果中
#     if not (cur.left or cur.right):
#         result.append(path)
#     if cur.right:
#         stack.append(cur.right)
#         path_st.append(path + '->' + str(cur.right.val))
#     if cur.left:
#         stack.append(cur.left)
#         path_st.append(path + '->' + str(cur.left.val))
#
# return result