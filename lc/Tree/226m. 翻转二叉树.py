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
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return

        # 我们把当前root的下面两个子节点给反转了，对所有的节点都执行这个操作
        # 最终结果就是所有节点都反转了
        root.left, root.right = root.right, root.left

        self.helper(root.left)
        self.helper(root.right)


