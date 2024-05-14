"""
有 n 个网络节点，标记为1到 n。

给你一个列表times，表示信号经过 有向 边的传递时间。times[i] = (ui, vi, wi)，其中ui是源节点，vi是目标节点， wi是一个信号从源节点传递到目标节点的时间。

现在，从某个节点K发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回-1 。

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
"""

import heapq
from collections import defaultdict
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # 初始化图，记录Key是每个点，value是可以到哪些目标点，以及到这些目标点的距离距离
        graph = defaultdict(list)
        for f, to, weight in times:
            graph[f].append((to, weight))

        # （start 到 当前节点最短距离，当前节点)。一开始初始化从最初起点出发，到自己节点的距离为0
        # 把距离放在前面是因为heap是根据第一个元素进行排序的
        heap = [(0, k)]

        visited = set()
        res = 0
        while heap:
            # pop出 从出发点到当前节点路径最短的点
            # 因为当这个from点更新完所有的相邻点后，则不再遍历这个节点了
            d1, cur = heapq.heappop(heap)

            # 假如当前点被遍历过, 那么我们直接跳过
            # 为什么我们下面已经用Visited过滤过，但还需要这个呢？
            # 因为有节点可能在被visit过之前，就已经被加进queue多次，所以后面会被多次遍历
            if cur in visited:
                continue
            # 当前点没被遍历过，则记录
            visited.add(cur)

            # 更新起点到其他点的最远距离
            res = max(res, d1)

            # 遍历当前节点所能到达的所有节点
            for to, d2 in graph[cur]:
                # 假如当前节点没被访问过，则进行访问(这个属于剪枝，可以去掉)
                if to not in visited:
                    heapq.heappush(heap, (d1 + d2, to))

        # 看看有没有遍历完整个图
        # 没遍历完则说明有点不可达
        if len(visited) != n:
            return -1
        return res
"""
time: E是times的长度，堆实现方式为O(ElogE),因为每个边都有可能被加进堆中
space: O(N+E) 图的大小是O(E) 加上其他对象的大小O(N)
"""
# 链接：https://www.youtube.com/watch?v=y_wHjstds4o

