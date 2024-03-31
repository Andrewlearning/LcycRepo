"""
有 n 个城市通过一些航班连接。给你一个数组flights ，其中flights[i] = [from[i], to[i], price[i]] ，
表示该航班都从城市 from[i] 开始，以价格 price[i] 抵达 to[i]。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k站中转的路线
使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。

输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
输出: 200

"""
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        import heapq
        from collections import defaultdict
        # key: 出发节点
        # value: (到达节点，花销)
        graph = defaultdict(list)
        for f, to, price in flights:
            graph[f].append((to, price))

        # (从起点到cur的花销，cur节点，总共有多少次转机次数)
        heap = [(0, src, k + 1)]

        # cur节点，从起点到cur的最多还剩转机次数
        res = {}
        while heap:
            d1, cur, steps = heapq.heappop(heap)
            # 记录当前节点，以及走到当前节点的步数
            res[cur] = steps

            # 假如到达终点
            if cur == dst:
                return d1

            # 假如还可以继续转机
            if steps > 0:
                for to, d2 in graph[cur]:
                    # 假如目的地我们没去过，我们需要探索
                    # 假如目的地我们去过，但我们有更优的方案到达这个目的地(转机次数更少)，那么我们需要继续探索
                    # 我们希望，每次push进heap中的，都是局部最佳的答案
                    if to not in res or steps > res[to]:
                        heapq.heappush(heap, (d1 + d2, to, steps - 1))

        return -1

"""
本题相当于在743的基础上，加了一个中转站点的限制
https://www.youtube.com/watch?v=y_wHjstds4o
"""