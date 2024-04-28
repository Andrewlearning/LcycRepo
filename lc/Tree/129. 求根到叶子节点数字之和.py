"""
给定一个二叉树，它的每个结点都存放一个0-9的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明:叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root, 0)
        return self.res

    def helper(self, root, cur):
        if not root:
            return

        cur *= 10
        cur += root.val

        # 当道根节点时，添加这条path的答案
        if not root.left and not root.right:
            self.res += cur
            return

        # 继续遍历
        self.helper(root.left, cur)
        self.helper(root.right, cur)

