"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
 and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
给定一个完全二叉树，求这个二叉树的节点数量，时间复杂 < O(n) 意味着不能单纯使用遍历，需要用到数学方法
完全二叉树: 如果二叉树除了最后一层有缺失外，其它是满的，且最后一层缺失的叶子结点只出现在右侧，则这样的二叉树叫完全二叉树
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        hl = hr = 1

        l = root
        while l.left != None:
            l = l.left
            hl += 1

        r = root
        while r.right != None:
            r = r.right
            hr += 1

        # 假如这棵树的最左，最右节点的高度都一样长的话，那么说明这是一颗满二叉树
        # 可以通过 2 ** height - 1 来获取该树的所有节点
        # 最差情况下该数只有一个节点，高度为1
        if hl == hr:
            return 2 ** (hl) - 1

        # 假如从当前root出发，下面并不是满二叉树，我们不能直接使用公式来计算节点，要分左右来处理
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

"""
time O(log2 N)
https://www.acwing.com/video/1594/
"""