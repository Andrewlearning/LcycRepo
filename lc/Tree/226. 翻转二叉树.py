"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9

过程
     4
   /   \
  7     2
 / \   / \
6   3 1   3

结果：
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        # 交换左右子树
        root.left, root.right = root.right, root.left

        # 递归处理左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


