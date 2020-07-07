"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.helper(p, q)

    def helper(self, root1, root2):
        # 当两个节点都不存在，说明判断完了，没出错
        if not root1 and not root2:
            return True

        # 一个节点存在，一个节点不存在，返回false
        if not root1 or not root2:
            return False

        # 两个节点值不一样
        if root1.val != root2.val:
            return False

        # 继续往下判断
        return self.helper(root1.left, root2.left) \
               and self.helper(root1.right, root2.right)