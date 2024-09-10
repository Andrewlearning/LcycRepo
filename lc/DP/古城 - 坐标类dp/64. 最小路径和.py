

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        lr = len(grid)
        lc = len(grid[0])

        # dp[i][j]表示从起点走到[i][j]的最小值
        dp = [[float('inf')] * lc for _ in range(lr)]

        for i in range(lr):
            for j in range(lc):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    # 假如i或j>0, 到[i][j]都有1条或2条路可以选
                    # 所以相当于我们选用更小的一条路，并记录
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j])
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])

        return dp[lr - 1][lc - 1]


"""
https://www.acwing.com/video/1402/
  // Time: O(m*n), Space: O(m*n)
"""

# 另一种做法，类似
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g = grid
        n = len(g)
        m = len(g[0])

        dp = [[0] * m for _ in range(n)]
        dp[0][0] = g[0][0]

        for i in range(n):
            for j in range(m):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + g[i][j]
                if i > 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + g[i][j]
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + g[i][j]

        return dp[-1][-1]