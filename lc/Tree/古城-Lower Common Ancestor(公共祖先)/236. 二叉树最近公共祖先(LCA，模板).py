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
        # base case1, 遍历最后都没有找到p,q的情况, 返回None
        if not root:
            return None
        # base case2, 遍历过程中找到p,q的情况，则返回p或q
        if root == p or root == q:
            return root

        """
        看在左子树和右子树里有没有找到pq
        case1. root.left, root.right刚好对应 p,q, 那么LCA就是root. 注意，在最终找到LCA的那一层遍历中，肯定是命中了这个case才能找到LCA
        case2. 在root.left里找到了LCA，那么LCA会被层层返回上来，所以left的值此时为LCA, right此时为None, 然后把left(LCA)返回出去
        case3. 在root.right里找到了LCA，那么LCA会被层层返回上来，所以right的值此时为LCA, left此时为None, 然后把right(LCA)返回出去
        """
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left
        if right:
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
