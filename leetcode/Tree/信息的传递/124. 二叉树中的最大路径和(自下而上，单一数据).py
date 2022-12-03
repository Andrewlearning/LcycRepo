"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。
该路径至少包含一个节点，且不一定经过根节点。
Example 1:
Input: [-1,2,3]

       -1
      / \
     2   3

Output: 2 + -1 + 3 = 4 ,包括树的任意节点哦!!
"""

import sys
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.res = float('-inf')
        self.helper(root)
        return self.res

    def helper(self, root):
        if root is None:
            return 0

        #这题有负数，所以我们在找子树的最大和时，一定要让max(子树和，0），避免负数入选
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)

        # 把经过当前节点的所有path都找出来，然后求出他们的最大值
        curSum = root.val + left + right

        # 记录最大值
        self.res = max(self.res, curSum)

        # 向上返回当前节点所计算得出的最大值
        return root.val + max(left, right)


"""
https://www.youtube.com/watch?v=10-xBLiytBA&t=95s 22:48
在每一个节点，都会往下遍历所有节点一次，所以时间复杂度和空间复杂度都是N^2

相似题型：
51
687
"""