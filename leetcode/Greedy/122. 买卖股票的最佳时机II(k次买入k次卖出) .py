"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit.
Note: You may not engage in multiple transactions(交易) at the same time
（当天可以有无数次 买入 卖出）
 当天的买入卖出其实一样，不影响你的收益
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0

        # 因为我们只能第一次卖出，产生收益，只能从第一天开始，因为是第0天买入
        for i in range(1,len(prices)):
            # 如果我们发现 今天的价格要比昨天的要高，那么我们就当买入昨天的，卖出今天的
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit

"""
time: On space: O1
"""