"""
给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

 

示例 1：
输入:

  5
 /  \
2   -3
返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 用一个hashmap去记录每个子树的和
        self.hashmap = collections.defaultdict(int)
        self.helper(root)

        res = []
        maxValue = -1
        for key, value in self.hashmap.items():
            if value > maxValue:
                res = [key]
                maxValue = value
            elif value == maxValue:
                res.append(key)

        return res

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)
        total = root.val + left + right
        self.hashmap[total] += 1

        return total