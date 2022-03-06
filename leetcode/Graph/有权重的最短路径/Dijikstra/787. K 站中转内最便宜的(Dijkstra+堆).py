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

        # key: 出发节点
        # value: (到达节点，花销)
        graph = collections.defaultdict(list)
        for f, to, weight in flights:
            graph[f].append((to, weight))

        # (从起点到cur的花销，cur节点，从起点到cur节点的当前路径选择的转机次数)
        heap = [(0, src, 0)]

        # key: cur节点
        # value: (从起点到cur节点的花销， 从起点到cur节点的当前路径选择的转机次数)
        dist = {src: (0, 0)}
        for to in range(n):
            if to != src:
                dist[to] = (float('inf'), float('inf'))

        while heap:
            d1, cur, times = heapq.heappop(heap)

            # 假如已经遍历到了目标节点，且转机次数没有超过限制，则返回结果
            if cur == dst and times <= k + 1:
                return d1


            for to, d2 in graph[cur]:
                # 只有当同时满足 新花销>=原最少花销 且 新转机次数>=原最小花销的转机次数
                # 才能跳过循环
                if d1 + d2 >= dist[to][0] and times + 1 >= dist[to][1]:
                    continue
                dist[to] = (d1 + d2, times + 1)
                heapq.heappush(heap, (d1 + d2, to, times + 1))

        return -1

"""
本题相当于在743的基础上，加了一个转接距离这样一个限制，将这个限制假如进heap 和 dist中再加以判断就好
https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/1477629/Python-DFS-and-Dijkstra-solutions-(beats-96)
"""