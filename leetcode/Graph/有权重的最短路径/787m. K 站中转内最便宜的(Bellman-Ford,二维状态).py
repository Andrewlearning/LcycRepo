"""
有 n 个城市通过 m 个航班连接。每个航班都从城市 u 开始，以价格 w 抵达 v。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到从 src 到 dst 最多经过 k 站中转的最便宜的价格。 如果没有这样的路线，则输出 -1。

输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
输出: 200

题目大意：给你一些城市之间的机票价格，问从src到dst的最少需要花多少钱，最多可以中转k个机场。
"""

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        maxCost = float("inf")
        # [使用了多少个中转城市][起点到第几个城市] 的最小花费
        cost = [[maxCost] * n for i in range(K + 2)]
        # [0个中转城市][起点到起点] 的最小花费是0
        cost[0][src] = 0


        for i in range(1, K + 2):
            cost[i][src] = 0
            for flight in flights:
                frm = flight[0]
                to = flight[1]
                weight = flight[2]
                # 当前中转城市的结果，是 上一个中转城市的结果+飞过来的花费
                cost[i][to] = min(cost[i][to], cost[i-1][frm] + weight)


        return -1 if cost[K+1][dst] >= maxCost else cost[K+1][dst]

"""
Time complexity: O(k * |flights|) / O(k*n^2)
Space complexity: O(k*n) -> O(n)

https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-787-cheapest-flights-within-k-stops/

"""