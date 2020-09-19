"""
给定一个二叉树，你需要找出二叉树中最长的连续序列路径的长度。

请注意，该路径可以是递增的或者是递减。例如，[1,2,3,4] 和 [4,3,2,1] 都被认为是合法的，而路径 [1,2,4,3] 则不合法。另一方面，路径可以是 子-父-子 顺序，并不一定是 父-子 顺序。

示例 2:

输入:
        2
       / \
      1   3
输出: 3
解释: 最长的连续路径是 [1, 2, 3] 或者 [3, 2, 1]。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root)

        return self.res

    def helper(self, root):
        if not root:
            return [0, 0]

        # status[0] 包含根节点的最长递增子序列的长度
        # status[1] 包含根节点的最长递减子序列的长度
        # 均初始化为 1
        status = [1] * 2

        left_status = self.helper(root.left)
        right_status = self.helper(root.right)

        if root.left:
            # 判断左子树处于连续递增序列中还是处于连续递减序列中
            if root.left.val + 1 == root.val:  # 处于连续递增序列中
                status[0] = left_status[0] + 1
            elif root.left.val - 1 == root.val:  # 处于连续递减序列中
                status[1] = left_status[1] + 1

        if root.right:
            # 判断右子树处于连续递增序列中还是处于连续递减序列中
            if root.right.val + 1 == root.val:  # 处于连续递增序列中
                status[0] = max(right_status[0] + 1, status[0])
            elif root.right.val - 1 == root.val:  # 处于连续递减序列中
                status[1] = max(right_status[1] + 1, status[1])

        # 把从根节点递增和递减的长度加在一起，因为根节点计算了两次，所以需要-1
        self.res = max(self.res, status[0] + status[1] - 1)
        return status