"""
给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。

所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        return self.helper(root, low, high)

    def helper(self, node, L, R):
        if not node:
            return None

        # 当前节点已经比右边界大了, 说明本节点及右子树都要剪掉
        if node.val > R:
            return self.helper(node.left, L, R)
        # 当前节点已经比左边界小了, 说明本节点及左子树都要剪掉
        elif node.val < L:
            return self.helper(node.right, L, R)
        # 当前节点没问题，那么可以分配一下，检测自己的子树有没有问题
        else:
            node.left = self.helper(node.left, L, R)
            node.right = self.helper(node.right, L, R)
            return node

"""
链接：https://leetcode-cn.com/problems/trim-a-binary-search-tree/solution/xiu-jian-er-cha-sou-suo-shu-by-leetcode/来源：力扣（LeetCode）
"""