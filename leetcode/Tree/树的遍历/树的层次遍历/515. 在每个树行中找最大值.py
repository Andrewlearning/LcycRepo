"""
您需要在二叉树的每一行中找到最大的值。

示例：

输入:

          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            temp = []
            levelMax = float("-inf")

            for node in queue:
                if node.val > levelMax:
                    levelMax = node.val

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            res.append(levelMax)
            queue = temp

        return res

