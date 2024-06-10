"""
给定一个整数数组，其中第i个元素代表了第i天的股票价格 。

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, hold):
            # base case, i=-1 -> 表示第0天开始
            if i < 0:
                # 第0天刚开始，持有股票, 不可能的case, 最大利润=-inf
                if hold:
                    return -inf
                # 第0天刚开始，不持有股票，最大利润=0
                else:
                    return 0

            # 第i天结束持有股票的最大值 = max(i-1天持有股票，i-2天未持有股票 + 第i天买入股票)
            # 这里是dfs(i - 2, False)的原因是 "卖出股票后，你无法在第二天买入股票"
            if hold:
                return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
            # 第i天结束未持有股票的最大值 = max(i-1天未持有股票，i-1天持有股票 + 第i天卖出股票)
            else:
                return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

        # 我们想知道第n-1天结束，且不持有股票的最大收益是多少
        return dfs(n - 1, False)

"""
时间复杂度
- 状态的个数是n+1天 * 2(买，卖)，单个状态的计算时间O(1)，所以总体时间复杂度是O(n)
空间复杂度
- 数组大小为 2 * n+1，所以空间复杂度是O(n)

# 参考自灵神的讲解
https://www.bilibili.com/video/BV1ho4y1W7QK/?spm_id_from=333.880.my_history.page.click&vd_source=b81616a45fd239becaebfee25e0dbd35
"""
