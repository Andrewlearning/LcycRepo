"""
有 n 个网络节点，标记为1到 n。

给你一个列表times，表示信号经过 有向 边的传递时间。times[i] = (ui, vi, wi)，其中ui是源节点，vi是目标节点， wi是一个信号从源节点传递到目标节点的时间。

现在，从某个节点K发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回-1 。

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
"""

import heapq
from collections import defaultdict
# dijkstra标准模板做法
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        from heapq import heappush, heappop

        graph = defaultdict(list)
        for f, to, weight in times:
            graph[f].append((to, weight))

        heap = [(0, k)]
        visited = [float('inf')] * (n + 1)
        visited[k] = 0

        while heap:
            d1, cur = heappop(heap)

            for to, d2 in graph[cur]:
                # 假如发现当前从 [起点~to] 的路径优于之前[起点~to]路径
                # 则更新[起点~to]的最短距离，并顺着这条路走下去
                if d1 + d2 < visited[to]:
                    visited[to] = d1 + d2
                    heappush(heap, (d1 + d2, to))

        # 从1开始，因为node是从1~n
        max_delay = max(visited[1:])
        if max_delay == float('inf'):
            return -1
        return max_delay

"""
时间复杂度
    构建图的时间复杂度为 O(E)
    最小堆操作(包括初始化和每次弹出、插入)的时间复杂度总和为 O(ElogV)
    - 因为每条边最多只会被松弛一次，因此总的松弛操作次数为E，每次操作的时间复杂度为O(logV).
        - 松弛(relaxation): 松弛操作的目的是通过检查和更新路径长度，从而找到从起点到所有其他节点的最短路径

空间复杂度
    存储图的邻接表'graph'需要 O(E)的空间。
    存储visited数组需要 O(V)的空间。
    最小堆的空间复杂度在最坏情况下为 O(V)。
    因此，总的空间复杂度为 - O(V+E)

古城算法链接：https://www.youtube.com/watch?v=y_wHjstds4o
"""

# dijkstra优化做法
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

# 古城算法链接：https://www.youtube.com/watch?v=y_wHjstds4o

