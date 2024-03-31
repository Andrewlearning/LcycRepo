"""
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        # 本题目的精华在这里
        # 我们通过频繁调用主函数，来使得每个节点都能经历一次从上往下的过程
        return self.helper(root, target) + self.pathSum(root.left, target) + self.pathSum(root.right, target)

    def helper(self, root, target):
        # 因为树的节点有可能是负数，所有不能加上 target < 0, 则退出循环的情况
        if not root:
            return 0

        target -= root.val
        res = 1 if target == 0 else 0
        return res + self.helper(root.left, target) + self.helper(root.right, target)
