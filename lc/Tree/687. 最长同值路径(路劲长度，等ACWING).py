"""
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:
2

示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:
2

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root)

        return self.res

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        left_arrow = right_arrow = 0
        if root.left and root.val == root.left.val:
            left_arrow = left + 1
        if root.right and root.val == root.right.val:
            right_arrow = right + 1

        self.res = max(self.res, left_arrow + right_arrow)

        return max(left_arrow, right_arrow)