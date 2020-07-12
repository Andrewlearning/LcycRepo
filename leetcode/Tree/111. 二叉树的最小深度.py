"""
给定一个二叉树，找出其最小深度
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        # 假如其中一边是None,那我们一定得走有节点的那边
        if not root.left or not root.right:
            return 1 + max(left, right)
        # 假如左右子树都有，那么我么要走深度小的那边
        else:
            return 1 + min(left, right)


