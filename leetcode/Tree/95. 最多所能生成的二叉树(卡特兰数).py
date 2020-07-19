"""
这题要求你把所有可能的二叉树都生成出来
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)

        # 这里的res不是全局变量，只存活在每次的辅助函数调用中，他返回了当前拥有节点
        # 所能组成的所有二叉搜索树
        return res

"""
https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/bu-tong-de-er-cha-sou-suo-shu-ii-by-leetcode/

这题思路和95是很像的，所谓最多能生成的二叉树，那我们就得用最少的点，这样才能生成
最多的树。 所以每棵树我们都只用三个节点
"""