"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
判断这棵树是不是二叉搜索树
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 中序遍历 left root right
        if not root:
            return True

        stack = []
        pre = -sys.maxsize
        cur = root

        while cur or stack:
            # 每次检查cur,cur.left,cur.right是否存在节点，都在这里检测
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop(-1)
            # 中序遍历，从小到大，所以node.val一定会比之前的大
            if cur.val <= pre:
                return False

            # 更新
            pre = cur.val
            cur = cur.right

        return True

# Time:O(n) Space:O(n)
# https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/