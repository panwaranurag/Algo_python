#Example
#  Input: [1, null, 2, 3]
#   1
#     \
#      2
#     /
#    3
#  Output: [3, 2, 1]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def postorder(self, root):
        res = []
        stack = [root]

        if root is None:
            return res

        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)

        return res