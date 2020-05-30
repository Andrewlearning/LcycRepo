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
        # 1. 当root == None, return None
        # 2. 当root == p, 说明p是作为父节点， q是作为 p的那那棵树的子节点
        # 3. 当root == q, 说明q是作为父节点， p是作为 q的那那棵树的子节点
        # 4。 有可能呈现一个分叉状， root 的左右两边都有 p == q == root, 这个时候说明 root就是公共祖先
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 情况4
        if left and right:
            return root

        # 情况2，3
        return left or right


"""
本题无法利用二叉搜索树的特性来写了
得用一种很巧妙的思路来写 -> root 和 p,q的关系

"""