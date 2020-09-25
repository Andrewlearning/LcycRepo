# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        queue = [[root, 0, 0]]

        res = cur_depth = left = 0

        for node, depth, pos in queue:

            if node:
                queue.append([node.left, depth + 1, pos * 2])
                queue.append([node.right, depth + 1, pos * 2 + 1])

                # 当二叉树的当前的高度 不等于当前node的高度，那么说明node已经进入了下一层
                if cur_depth != depth:
                    # 因为进入了下一层，所以我们要更新cur_depth
                    cur_depth = depth

                    # 同时把这一层的最左节点，记录下来
                    left = pos

                # 每一层的宽度等于 最右节点 - 最左节点 + 1
                res = max(res, pos - left + 1)

        return res

"""
https://leetcode-cn.com/problems/maximum-width-of-binary-tree/
时间复杂度： O(N)，其中 N 是输入树的节点数目，我们遍历每个节点一遍。
空间复杂度： O(N)，这是 queue 的大小。
"""
