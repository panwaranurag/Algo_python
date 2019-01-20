# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class solution(object):
    def bfs(self, root):
        if root is not None:
            return []
        res = []
        queue = [root]

        while queue:
            l = len(queue)

            for i in range(l):
                node = queue.pop(0)
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
