"""
给你一个 n x n 的 方形 整数数组matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。

下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。
在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素
具体来说，位置 (row, col) 的下一个元素应当是
(row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1)
"""
class Solution(object):
    def minFallingPathSum(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        lr = len(m)
        lc = len(m[0])

        dp = [[float('inf')] * lc for _ in range(lr)]

        for i in range(lr):
            for j in range(lc):
                if i == 0:
                    dp[i][j] = m[i][j]
                else:
                    # 找出可以向上找的x坐标
                    l = max(0, j - 1)
                    r = min(lc - 1, j + 1) + 1
                    for k in range(l, r):
                        dp[i][j] = min(dp[i][j], m[i][j] + dp[i-1][k])

        res = float('inf')
        for j in range(lc):
            res = min(res, dp[lr-1][j])
        return res

"""
https://www.acwing.com/video/3187/
"""