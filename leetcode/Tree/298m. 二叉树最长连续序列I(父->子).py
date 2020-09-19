"""
给你一棵指定的二叉树，请你计算它最长连续序列路径的长度。
该路径，可以是从某个初始结点到树中任意结点，通过「父 - 子」关系连接而产生的任意路径。
这个最长连续的路径，必须从父结点到子结点，反过来是不可以的。(必须要是从上到下递增才可以)

示例 1：

输入:

   1
    \
     3
    / \
   2   4
        \
         5

输出: 3
解析: 当中，最长连续序列是 3-4-5，所以返回结果为 3
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.res = 0
        self.helper(root, -1, 0)
        return self.res

    def helper(self, root, pre, length):
        if root is None:
            return

        if root.val == pre + 1:
            length += 1
        else:
            length = 1

        if length > self.res:
            self.res = length

        self.helper(root.left, root.val, length)
        self.helper(root.right, root.val, length)

# https://www.youtube.com/watch?v=XPxJQAI2mDA