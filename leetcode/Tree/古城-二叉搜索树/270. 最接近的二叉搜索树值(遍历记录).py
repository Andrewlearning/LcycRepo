"""
给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。

注意：

给定的目标值 target 是一个浮点数
题目保证在该二叉搜索树中只会存在一个最接近目标值的数
示例：

输入: root = [4,2,5,1,3]，目标值 target = 3.714286

    4
   / \
  2   5
 / \
1   3

输出: 4
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.diff = float("inf")
        self.res = None
        self.helper(root, target)
        return self.res.val

    # 遍历所有节点，并记录最小的差值
    def helper(self, root, target):
        if not root:
            return

        if abs(target - root.val) < self.diff:
            self.diff = abs(target - root.val)
            self.res = root

        self.helper(root.left, target)
        self.helper(root.right, target)
