"""
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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

        minprice = sys.maxsize
        maxprofit = 0

        for price in prices:
            # 我们不断更新股票的历史最低价格
            minprice = min(minprice, price)

            # 任何一个当前价格都有可能是历史最高价格，所以要不断尝试
            maxprofit = max(maxprofit, price - minprice)

        return maxprofit

"""
我们可以维持两个变量——minprice 和 maxprofit
它们分别对应迄今为止所得到的最小的谷值和最大的利润（卖出价格与最低价格之间的最大差值）。
"""