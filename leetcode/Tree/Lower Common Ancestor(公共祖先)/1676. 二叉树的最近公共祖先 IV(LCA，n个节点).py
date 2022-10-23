"""
我们需要为多个目标节点(>3)，找到他们的最近公共祖先
All the nodes will exist in the tree
and all values of the tree's nodes are unique.
"""
class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: TreeNode
        :rtype: TreeNode
        """
        s = set()
        for node in nodes:
            s.add(s)
        return self.lca(root, s)

    # 其实解决办法和两个节点是一样，我们需要找到第一个分叉点
    # 因为树只有两个left, right两边，只要两边都存在set里的节点，那么则是这个节点
    def lca(self, root, s):
        if root == None:
            return None
        if root in s:
            return root

        left = self.lca(root.left, s)
        right = self.lca(root.right, s)

        if left and right:
            return root
        if left != None:
            return left
        if right != None:
            return right
        return None