"""
Given a binary tree, find the lowest common ancestor (LCA)(最近公共祖先)
 of two given nodes in the tree.

"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
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
        # 说明那两个节点在左右子树的其中一边，所以最低公共父节点不在这一层，可能在更上一层或在更下一层
        if left is not None:
            return left
        if right is not None:
            return right
        # 假如都没找到, return None
        return None



"""   6
    5    8
   3  2
        1   
答案：
因为每个node都只遍历一次，所以Time:O(n) , Space:O(n)
"""
