"""
假如有一排房子，共 n 个，每个房子可以被粉刷成 k 种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x k 的矩阵来表示的。

例如，costs[0][0] 表示第 0 号房子粉刷成 0 号颜色的成本花费；costs[1][2] 表示第 1 号房子粉刷成 2 号颜色的成本花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。

输入: [[1,5,3],
      [2,9,4]]

输出: 5
解释: 将 0 号房子粉刷成 0 号颜色，1 号房子粉刷成 2 号颜色。最少花费: 1 + 4 = 5;
     或者将 0 号房子粉刷成 2 号颜色，1 号房子粉刷成 0 号颜色。最少花费: 3 + 2 = 5.
"""
import sys


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        if not costs and len(costs) == 0:
            return 0

        # n个房子
        n = len(costs)

        # 每个房子可以被刷成k种颜色
        k = len(costs[0])

        # dp[n][k] 有N个房子，每个房子可以有K个颜色
        # dp[n][k] 是选定当前第n个房子的k个颜色，所能形成的最小值
        dp = [[0] * k for i in range(n)]

        # 初始化
        for i in range(n):
            dp[0][j] = costs[0][j]

        for i in range(1, n):
            for j in range(k):

                # 记录每个房子上一层的最小值
                min_lastlevel = sys.maxsize

                # 找到每个房子上一层的最小值
                for c in range(k):
                    if c != j:
                        min_lastlevel = min(min_lastlevel, dp[i - 1][c])

                # 找到上一层的最小值 + 当前行值 = dp[i][j]
                dp[i][j] = min_lastlevel + costs[i][j]

        return min(dp[-1])


"""
// Time: O(n*k^2), Space: O(n*k)
https://algocasts.io/episodes/VlWdLOW0
思路与粉刷房子1基本一样，这里不考虑各种优化的写法
"""