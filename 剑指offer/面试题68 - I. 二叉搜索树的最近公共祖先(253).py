"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # 利用二叉搜索树的特性，根据值的大小来进行查找

        # p,q值都比 root小，说明p,q都在root的左边
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p.val, q.val)
        # p,q值都比 root小，说明p,q都在root的右边
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p.val, q.val)

        # 出现分叉则说明，公共祖先节点在root上
        return root