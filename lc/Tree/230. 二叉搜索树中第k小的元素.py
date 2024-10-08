# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def kthSmallestStack(self, root, k):
        res = 0
        stack = []

        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop(0)
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right



"""
我们对这题考虑使用中序遍历法，因为是按顺序的
递归：
时间复杂度：O(N)，遍历了整个树。
空间复杂度：O(N)，用了一个数组存储中序序列。
"""


