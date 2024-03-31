"""
Given an integer n, return all the structurally unique BST's (binary search trees),
 which has exactly n nodes of unique values from 1 to n.
 Return the answer in any order.
这题要求你把所有可能的二叉搜索树都生成出来

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []

        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None]

        res = []

        for i in range(start, end + 1):
            # 我们以每个i作为root节点，然后对root两边的节点分而治之
            left = self.helper(start, i - 1)
            right = self.helper(i + 1, end)

            # 把所有左子树找出来
            for l in left:
                # 把所有右子树找出来
                for r in right:
                    # 拼凑起来
                    # 这里剩最后一个node的时候，左子树和右子树都为空。
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)

        return res

"""
https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/bu-tong-de-er-cha-sou-suo-shu-ii-by-leetcode/
"""