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
            # 当前持有股票的最大利润
            # 由于我们每次都从第一天开始算，我们都假设在第0天购买了股票
            max_diff = -prices[0]

            for i in range(1, n):
                # dp[i - 1][j], 表示在0 - i-1天最多进行j次买卖时的最大利润, 且在第i天不买卖股票
                # max_diff + prices[i], [0~i-1]天持有股票时的最大利润 + 第i天卖出股票的利润
                dp[i][j] = max(dp[i - 1][j], max_diff + prices[i])

                # 更新当前持有股票的最大利润
                # 0-i天且当前已经持有股票的最大利润
                # 在第i天之前已经不持有股票，在第i-1天进行j-1次买卖时的最大利润 + 购买股票并减去当天的价格
                max_diff = max(max_diff, dp[i - 1][j - 1] - prices[i])

        return dp[-1][k]

"""
跟acwing思路接近
来自宋姐: https://github.com/Christinezy/Leetcode/blob/main/Dp/%E5%A4%9A%E7%BB%B4%E7%8A%B6%E6%80%81dp%E9%97%AE%E9%A2%98/188.%20%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA%20IV.py
"""

