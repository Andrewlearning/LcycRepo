"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
"""
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # 本题的手续费，在买入时-fee, 还是到卖出时才-fee, 对结果都不会影响

        # dp[第几天][0没有股票，1持有股票]
        dp = [[0, 0] for _ in range(len(prices))]

        # 第0天不持有股票，利润为0
        dp[0][0] = 0

        # 第0天并持有股票，说明买入了第0天的股票
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            # 今天手里没股票，说明是昨天就没了，或者是今天才卖的
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)

            # 今天手里有股票，说明是昨天就有了，或者是今天才买的
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]

    # https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/dong-tai-gui-hua-by-liweiwei1419-6/
