"""
给定一棵二叉树，再给定两个节点（未必在树中），求这两个节点的最近公共祖先。
题目保证节点的数字各不相同
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 首先先确定p, q这两个节点在树里面是否存在
        findP = self.dfs(root, p)
        findQ = self.dfs(root, q)
        # 假如其中一个不存在则返回None
        if findP is None or findQ is None:
            return None
        # 假如都存在则使用LCA模板去找
        else:
            return self.lca(root, p, q)

    # 后续遍历所有节点，left right root
    def dfs(self, root, target):
        if root is None:
            return None
        if root.val == target:
            return root

        left = self.dfs(root.left, target)
        right = self.dfs(root.right, target)

        # 返回找到的节点
        return left or right

    def lca(self, root, p, q):
        # 1. 遍历到 p,q的情况，则返回p 或 q
        # 2. 遍历到None的情况(说明没找到pq),则返回None
        if (not root) or (root == p) or (root == q):
            return root

        # 看左子树和右子树有没有找到pq
        # 假如说只有一遍找到的话，被找到的节点肯定是最近公共祖先，因为他最先被找到，且另外一个节点
        # 肯定在它下面
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 假如左右子树都找到pq,说明两个节点肯定在当前节点的一左一右，返回当前root，作为LCA
        if left and right:
            return root
        # 假如说只找到p, q中的一个，则返回p或q
        if left is not None:
            return left
        if right is not None:
            return right
        # 假如都没找到, return None
        return None
        
