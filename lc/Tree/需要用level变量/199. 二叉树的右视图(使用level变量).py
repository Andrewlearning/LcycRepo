# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            nxt = []
            n = len(queue)
            res.append(queue[-1].val)

            while n:
                cur = queue.pop(0)
                if cur.left:
                    nxt.append(cur.left)
                if cur.right:
                    nxt.append(cur.right)
                n -= 1

            queue = nxt

        return res

"""
On On
二叉树的层序遍历，每次只取最右边的点
"""