"""
举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。

如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        s1 = self.helper(root1, [])
        s2 = self.helper(root2, [])
        return s1 == s2

    def helper(self, root, res):
        if not root:
            return 0

        if not root.left and not root.right:
            res.append(root.val)

        self.helper(root.left, res)
        self.helper(root.right, res)

        return res
