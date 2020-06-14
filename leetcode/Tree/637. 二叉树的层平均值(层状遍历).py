"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:

输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            # queue用来装这一层需要遍历的元素 以及下一层需要装进去的元素

            # temp用来当前这一层的结果
            temp = []

            # 我们用这个for 循环锁住了queue的取值范围，所以后面无论怎么放都不会影响到
            # 我们当前这一层的情况
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(sum(temp)*1.0 / len(temp))

        return res