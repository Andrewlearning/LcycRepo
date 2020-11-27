"""
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""
import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        maxprofit = 0
        low = sys.maxsize

        for price in prices:
            # 因为要做到低买高卖
            if price < low:
                low = price

            # low, 总是记录着前面所有最低价的状态，代表的意思是低买
            # 然后我们这里做的判断是，当前的价格 - 之前最低的价格
            # 那么就是低买高卖的意思
            if price - low > maxprofit:
                maxprofit = price - low

        return maxprofit