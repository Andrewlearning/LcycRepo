"""
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        minprice = sys.maxsize
        maxprofit = 0

        for price in prices:
            # max(历史最大profit, 当日价格 - 之前该股最低价格)
            maxprofit = max(maxprofit, price - minprice)

            # 我们更新股票的历史最低价格
            minprice = min(minprice, price)

        return maxprofit

"""
这是贪心做法
我们可以维持两个变量——minprice 和 maxprofit
它们分别对应迄今为止所得到的最小的谷值和最大的利润（卖出价格与最低价格之间的最大差值）。
"""