"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        # dp[第几天][0没有股票，1持有股票]
        dp = [[0, 0] for _ in range(len(prices))]

        # 第0天不持有股票，利润为0
        dp[0][0] = 0

        # 第0天并持有股票，说明买入了第0天的股票
        dp[0][1] = -prices[0]

        # 第1天不持有股票，max(0天没买，0天买今天卖)
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])

        # 第一天持有股票，max(0天买，今天买)
        dp[1][1] = max(dp[0][1], -prices[1])

        for i in range(2, len(prices)):
            # 今天手里没股票，说明是昨天就没了，或者是今天才卖的
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])

            # 考虑到买股票有冷冻期，说明今天可以买的话，那么是两天前卖的
            # 今天手里有股票，说明是昨天就有了，或者是今天才买的
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[-1][0]

# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/zui-jia-mai-mai-gu-piao-shi-ji-han-leng-dong-qi-py/
