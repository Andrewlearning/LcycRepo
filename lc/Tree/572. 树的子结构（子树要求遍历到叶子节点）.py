# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isSubtree(self, s, t):
        if not s:
            return False
        if self.helper(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def helper(self, s, t):
        # 说明两个树的节点都找完了，但是没出现问题，返回True
        # 这里和剑指26不太一样
        if not s and not t:
            return True

        # 一个树的节点找完了，另一个树的节点没找完，返回False
        if not s or not t:
            return False

        # 比较当前节点的值，并且继续比较下去
        return s.val == t.val and self.helper(s.left, t.left) and self.helper(s.right, t.right)

"""
本题是，要求 父树的所有节点，在子树上都有体现
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

本题可以对照剑指offer26题树的子结构看

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4 
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。


示例2 对于剑指26题来说是正确的
示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。
"""