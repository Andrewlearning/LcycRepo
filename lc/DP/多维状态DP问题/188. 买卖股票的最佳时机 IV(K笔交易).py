"""
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
"""

"""
定义 
dfs(i,j,0) 表示到第i天结束时完成至多j笔交易，未持有股票的最大利润
dfs(i,j,1) 表示到第i天结束时完成至多j笔交易，持有股票的最大利润

如何算一次交易: 
买和卖都完成了才算一次交易
所以可以把j-1放在买入流程或者是卖出流程中，下面是在买入时就把交易次数-1
dfs(i,j,0)= max(dfs(i-1,j,0), dfs(i-1,j,1) + prices[i])
dfs(i,j,1)= max(dfs(i-1,j,1), dfs(i-1,j-1,0) - prices[i])

递归边界:
dfs(·,-1,·) =-inf 任何情况下，j都不能为负，不能完成负数次交易
dfs(-1,j,0) = 0   第0天开始未持有股票，利润为0
dfs(-1,j,1) =-inf 第0天开始不可能持有股票

递归入口:
max(dfs(n-1,k,0), dfs(n-1,k,1)) 
= dfs(n-1,k,0)，由于最后一天手里肯定没股票的时候收益才可能是最大的
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, j, hold):
            # 递归边界
            # 完成-1笔交易，不可能，返回-inf
            if j < 0:
                return -inf

            # 递归边界
            # i = -1 case, 说明第0天开始
            if i < 0:
                # 第0天开始持有股票，不可能的情况，返回-inf
                if hold:
                    return -inf
                # 第0天开始没持有股票，利润为0，返回0
                else:
                    return 0

            # 第i天结束交易j次持有股票的最大值 = max(i-1天交易j次持有股票，i-1天交易j-1次未持有股票 + 第i天买入股票)
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
            # 第i天结束交易j次未持有股票的最大值 = max(i-1天交易j次未持有股票，i-1天交易j次(不用-1，已在买入时计算过)持有股票 + 第i天卖出股票)
            else:
                return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])

        # 递归入口，最后一天结束，完成j笔交易，未持有股票的最大利润
        return dfs(n - 1, k, False)

"""
1:1 翻译成递推
f[i][j][0] = max(f[i-1][j][0], f[i-1][j][1] + prices[i])
f[i][j][1] = max(f[i-1]|j][1], f[i-1][j-1][0] - prices[i])
由于i和j都有=0的情况，但没有办法表示 f[-1][.][.] 和 f[·][-1][.] 这两个状态
那就在f 和每个 f[i] 的最前面插入一个状态

最终递推式
f[.][0][.] = -inf, 表示到无论在第几天且是否持有股票，交易次数为-1时最大利润，为-inf(不可能的情况)
f[0][j][0] = 0,    j>=1 表示到第0天开始时，未持有股票的最大利润，为0
f[0][j][1] = -inf, j>=1 表示到第0天开始时，持有股票的最大利润，为-inf(不可能的情况)

f[i + 1][j][0] = max(f[i][j][0], f[i][j][1] + prices[i])
f[i + 1][j][1] = max(f[i][j][1], f[i][j-1][0] - prices[i])
答案为 f[n][k+1][0]
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # base case
        # f[.][0][.] = -inf, 表示到无论在第几天且是否持有股票，交易次数为-1时最大利润，为-inf(不可能的情况)
        # 最后我们return的结果是 f[n][k+1][0]
        f = [[[-inf] * 2 for _ in range(k + 2)] for _ in range(n+1)]

        # base case
        # f[0][j][0] = 0, j >= 1
        # 表示到第0天开始时，未持有股票的最大利润，为0
        # f[0][j][1] = -inf, j >= 1
        # 表示到第0天开始时，持有股票的最大利润，为 - inf(不可能的情况)
        for j in range(1, k+2):
            f[0][j][0] = 0

        for i, p in enumerate(prices):
            for j in range(1, k+2):
                # 第i天结束交易j次未持有股票的最大值 = max(i-1天交易j次未持有股票，i-1天交易j次(不用-1，已在买入时计算过)持有股票 + 第i天卖出股票)
                f[i+1][j][0] = max(f[i][j][0], f[i][j-1][1] + p)
                # 第i天结束交易j次持有股票的最大值 = max(i-1天交易j次持有股票，i-1天交易j-1次未持有股票 + 第i天买入股票)
                f[i+1][j][1] = max(f[i][j][1], f[i][j][0] - p)

        return f[n][k+1][0]


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        # 创建一个二维数组dp，dp[i][j]表示在第i天最多进行j次买卖时的最大利润
        # dp[i][j] 已经表示手里没有股票了，都卖掉了，相当于省略掉了一个记录买卖的状态
        dp = [[0] * (k + 1) for _ in range(n)]

        for j in range(1, k + 1):
            # 在第i-1天持有股票时的最大利润
            # 由于我们每次都从第一天开始算，我们都假设在第0天购买了股票
            max_diff = -prices[0]

            for i in range(1, n) :
                # dp[i - 1][j], 表示在0 - i-1天最多进行j次买卖时的最大利润, 且在第i天不买卖股票
                # max_diff + prices[i], [0~i-1]天持有股票时的最大利润 + 第i天卖出股票的利润
                dp[i][j] = max(dp[i - 1][j], max_diff + prices[i])

                # 更新当前第i天持有股票的最大利润
                # 0-i天且当前已经持有股票的最大利润
                # 在第i天之前已经不持有股票，在第i-1天进行j-1次买卖时的最大利润 + 购买股票并减去当天的价格
                max_diff = max(max_diff, dp[i - 1][j - 1] - prices[i])

        return dp[-1][k]

"""
跟acwing思路接近
来自宋姐: https://github.com/Christinezy/Leetcode/blob/main/Dp/%E5%A4%9A%E7%BB%B4%E7%8A%B6%E6%80%81dp%E9%97%AE%E9%A2%98/188.%20%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA%20IV.py
"""