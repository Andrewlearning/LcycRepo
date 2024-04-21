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
        res = 0

        # 因为我们只能第一次卖出，产生收益，只能从第一天开始，因为是第0天买入
        for i in range(1,len(prices)):
            # 如果我们发现 今天的价格要比昨天的要高，那么我们就当买入昨天的，卖出今天的

            # 一个困惑点，这个算法如何思考[0,1,2,3,4]这种情况
            # 在i=1的时候，卖出股票，赚到1-0=1
            # 在i=2的时候，买入p=1的是股票，卖出p=2的股票，赚到2-1=1
            # 这样的计算方式相当于i=1的股票没卖
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]

        return res

"""
time: On space: O1
使用贪心的思路，只要后一天的价格>前一天，则进行买卖
"""