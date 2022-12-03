"""
给你一棵二叉树的根节点 root，找出这棵树的 每一棵 子树的 平均值 中的 最大 值。
子树是树中的任意节点和它的所有后代构成的集合。
树的平均值是树中节点值的总和除以节点数。

输入：[5,6,1]
输出：6.00000
解释：
以 value = 5 的节点作为子树的根节点，得到的平均值为 (5 + 6 + 1) / 3 = 4。
以 value = 6 的节点作为子树的根节点，得到的平均值为 6 / 1 = 6。
以 value = 1 的节点作为子树的根节点，得到的平均值为 1 / 1 = 1。
所以答案取最大值 6。
"""
class Solution:
    def maximumAverageSubtree(self, root):
        self.res = 0.0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return [0.0, 0]

        curRes = 2 * [0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        # sum
        curRes[0] = left[0] + right[0] + root.val
        # count
        curRes[1] = left[1] + right[1] + 1
        self.res = max(self.res, curRes[0] / curRes[1])

        return curRes
