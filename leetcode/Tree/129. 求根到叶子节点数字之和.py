"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

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
        self.helper(root, "")

        return self.res

    def helper(self, root, string):
        if not root:
            return 0

        # 当到叶子节点的时候，把每回合拼在一起的字符加进res里去
        if not root.left and not root.right:
            self.res += int(string + str(root.val))
            return


        if root.left:
            # 之前节点的字符 + 当前节点的值
            self.helper(root.left, string + str(root.val))
        if root.right:
            self.helper(root.right, string + str(root.val))

