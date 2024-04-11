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

        # 这题有负数，所以我们在找子树的最大和时，一定要让max(子树和，0），避免负数入选
        # 选中0的时候，表示root.left子树和是为负数，相当于不计算root.left所有节点
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)

        # 把经过当前节点的所有path都找出来，然后求出他们的最大值
        curSum = root.val + left + right

        # 记录最大值
        self.res = max(self.res, curSum)

        """
        向上返回当前节点所计算得出的最大值
        由于对path的定义，是不能出现折返的，例如 a -> b -> c ，只有abc 或 abd算path, abcd是不算的
                                                  \> d
        所以需要返回max(left, right)
        """
        return root.val + max(left, right)


"""
https://www.youtube.com/watch?v=10-xBLiytBA&t=95s 22:48
在每一个节点都可以作为起点，同时每一个节点也都可以作为终点，所以所以遍历所有起点到所有终点的可能性是n*n
所以时间复杂度和空间复杂度都是N^2

相似题型：
51
687
"""