"""
给定一个整数数组prices，其中第i个元素代表了第i天的股票价格 ；非负整数fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润:((8 - 1) - 2) + ((9 - 4) - 2) = 8.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0] * 2 for _ in range(n + 1)]

        # 初始状态
        # 第0天开始且持有股票是不可能的，所以是-inf
        # 第0天开始且不持有股票，是默认值0
        dp[0][1] = -inf

        for i, p in enumerate(prices):
            # 第i天结束未持有股票的最大值 = max(i-1天未持有股票，i-1天持有股票 + 第i天卖出股票)
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + p)

            # 第i天结束持有股票的最大值 = max(i-1天持有股票，i-1天未持有股票 + 第i天买入股票 - 买股票的手续费)
            # 因为交易 = 买入1次 + 卖出一次，一次交易只收一次交易费，所以我们把交易费放在买入的时候扣或卖出的时候扣都可以
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - p - fee)

        # 返回第n-1天结束且未持有股票的值(理论上的最大值)
        return dp[n][0]


# 这个的遍历顺序是从后往前，在遍历到最前的时候生成base case, 然后从前往后生成结果
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        @cache
        def dfs(i, hold):
            # 递归边界
            # i = -1 case, 说明第0天开始
            if i < 0:
                # 第0天开始持有股票，不可能的情况，返回-inf
                if hold:
                    return -inf
                # 第0天开始没持有股票，利润为0，返回0
                else:
                    return 0

            # 第i天结束持有股票的最大值 = max(i-1天持有股票，i-1天未持有股票 + 第i天买入股票 - 买股票的手续费)
            # 因为交易 = 买入1次 + 卖出一次，一次交易只收一次交易费，所以我们把交易费放在买入的时候扣或卖出的时候扣都可以
            if hold:
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i] - fee)
            # 第i天结束未持有股票的最大值 = max(i-1天未持有股票，i-1天持有股票 + 第i天卖出股票)
            else:
                return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

        # 递归入口，最后一天结束且未持有股票
        return dfs(n - 1, False)

"""
时间复杂度
- 状态的个数是n+1天 * 2(买，卖)，单个状态的计算时间O(1)，所以总体时间复杂度是O(n)
空间复杂度
- 数组大小为 2 * n+1，所以空间复杂度是O(n)
"""