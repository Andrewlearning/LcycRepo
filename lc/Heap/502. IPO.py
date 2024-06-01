"""
k 表示能选择几个项目
w 表示有多少资本
profits 表示每个项目的利润有多少
captital 表示每个项目要有多少资本才会参与

目标是能得到最多的资本

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
只能选择两个项目，且第二第三个项目的参与门槛是一样的，都是1，且第三个项目利润高
所以
1、先选择第一个项目，因为没有参与成本，获得利润1
2、选择第三个项目，获得利润3
所以总共资本为1 + 3=4
"""

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        from heapq import heappush, heappop

        n = len(profits)

        # 由于项目有资本门槛，所以我们先按资本门槛排序，然后再按项目的利润排序
        # 这样就能保证假如两个项目资本门槛相同，我们能优先选择到利润高的
        # pjs = []
        # for i in range(n):
        #     pjs.append([capital[i], profits[i]])
        pjs = list(zip(capital, profits))
        pjs.sort()

        # 创建一个heap, 里面存放目前资本可以做的项目
        hp = []
        i = 0
        for _ in range(k):
            # 把达到当前门槛的先都加进heap里
            while i < n and pjs[i][0] <= w:
                profit = pjs[i][1]
                # 我们要让利润大的项目排在前面
                heappush(hp, -profit)
                i += 1

            if len(hp) == 0:
                break

            # 记录当前可做的项目
            curMaxProfit = -1 * heappop(hp)
            w += curMaxProfit

        return w

"""
时间复杂度
- 排序的时间复杂度为 O(nlogn)，堆每次操作的时间复杂度为 O(logn)，故总时间复杂度为 O(nlogn)
空间复杂度
- 需要额外 O(n)的空间存储堆
https://www.acwing.com/activity/content/problem/content/2924/
"""