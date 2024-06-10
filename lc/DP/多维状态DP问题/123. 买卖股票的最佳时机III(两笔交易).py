"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).


Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
(最多有两次交易,买和卖合在一起算一次交易)，这题递归就需要有三个状态了
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)

        # 0~i最小的股票价格
        preMin = float('inf')
        # 从[0~i]，只买卖一次股票的最大收益
        f = [0] * n

        # 我们先构造f
        for i in range(n):
            curMax = prices[i] - preMin
            if i > 0:
                f[i] = max(f[i-1], curMax)
            # 记录从0到当前位置的最小股票价格
            preMin = min(preMin, prices[i])

        # 记录从当前[i ~ -1]的最大股票价格
        maxPriceForward = float('-inf')

        # 初始状态设置为从0 ~ n-1只交易一次的最大利润
        # 存在一种可能只交易一次的结果就是最好的，例如[1,2,3,4]
        # 所以要设置为这个值
        res = f[n - 1]

        # 遍历范围到n-1 ~ 1是因为f[i-1]
        for i in range(n - 1, 0, -1):
            if maxPriceForward > prices[i]:
                # maxPriceForward - prices[i] 为 i ~ -1 的最大利润
                # f[i - 1] 为 0 ~ i-1 的最大利润
                # 我们有了这两次交易的最大利润，就可以得到题目所要的结果
                res = max(res, maxPriceForward - prices[i] + f[i - 1])
            maxPriceForward = max(maxPriceForward, prices[i])
        return res

"""
acwing: https://www.acwing.com/activity/content/problem/content/2551/

本题使用灵神模板会超空间，得使用db的压缩空间的方式才能通过
"""