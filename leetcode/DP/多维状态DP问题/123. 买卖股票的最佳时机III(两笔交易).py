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
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0


        # [第几天][交易第几次(卖出股票多少次)][手上有股票1，手上没股票0]
        profit = [[[0 for i in range(2)] for i in range(3)] for i in range(len(prices))]

        # 第0天，0次交易，手上没股票，所以收益为0
        profit[0][0][0] = 0

        # 第0天，0次交易，手上有股票，所以收益为-prices[0]
        profit[0][0][1] = -prices[0]

        # 第0天，1次买卖，手上有没股票都是不可能的，因为在第0天不可能同时完成买卖两次操作
        profit[0][1][0], profit[0][1][1] = -sys.maxsize, -sys.maxsize

        # 第0天，2次买卖，手上有没股票都是不可能的，因为在第0天不可能同时完成买卖两次操作
        profit[0][2][0], profit[0][2][1] = -sys.maxsize, -sys.maxsize


        for i in range(1, len(prices)):
            # 0买0卖，不进行交易的话，那么还是等于上一天的情况
            profit[i][0][0] = profit[i-1][0][0]

            # 1买0卖，手头上有股票，可能是上一天买的，也有可能是这一天买的
            profit[i][0][1] = max(profit[i-1][0][1], profit[i-1][0][0] - prices[i])


            # 1买1卖，手头上没股票，说明上一天卖了，或者是这一天卖了
            profit[i][1][0] = max(profit[i-1][1][0], profit[i-1][0][1] + prices[i])

            # 2买1卖，手头上有股票，说明上一天买了，或者是这一天买了
            profit[i][1][1] = max(profit[i-1][1][1], profit[i-1][1][0] - prices[i])

            # 2买2卖，手头上没股票（不可能再买了），看股票之前卖赚的多还是现在卖赚最多
            profit[i][2][0] = max(profit[i-1][2][0], profit[i-1][1][1] + prices[i])

        end = len(prices) - 1


        # 中间都是0是因为，手上没股票了，利润才可能是最大的
        return max(profit[end][0][0], profit[end][1][0], profit[end][2][0])

"""
profit[i][k][j]
这个递推有三个状态，i = 天数，  k = 之前交易了多少次,          j = 目前是持有还是不持有股票,还是已经到了买卖限制了 
                i (0-n-1)    k (0,k)k表示总交易次数的限制   j (0,1)                                   

假如说题目要求可以持有多只股票，那么j的含义可以变成目前持有多少只股票
"""