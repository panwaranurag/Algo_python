#Example
#  Input: [1, null, 2, 3]
#   1
#     \
#      2
#     /
#    3
#  Output: [1, 2, 3]

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorder(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)