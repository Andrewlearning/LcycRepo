"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return

        self.helper(root.left)

        # 其实这道题就是遍历整个树，但是我们要怎么区分哪里的叶子节点呢？
        # 就是从这个if 语句来判断，直接只查左边的树
        if root.left:
            if not root.left.left and not root.left.right:
                self.res += root.left.val
        self.helper(root.right)

# https://www.acwing.com/video/1800/