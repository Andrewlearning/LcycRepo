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

        q = [root]
        res = []

        while q:
            temp = []
            for i in range(len(q)):
                node = q[i]
                if i == len(q) - 1:
                    res.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp
        return res

"""
On On
二叉树的层序遍历，每次只取最右边的点, acwing也是这样写
"""