"""
有 n 个网络节点，标记为1到 n。

给你一个列表times，表示信号经过 有向 边的传递时间。times[i] = (ui, vi, wi)，其中ui是源节点，vi是目标节点， wi是一个信号从源节点传递到目标节点的时间。

现在，从某个节点K发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回-1 。
"""

import heaheap
import collections


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # 初始化图，记录Key是每个点，value是可以到哪些目标点，以及到这些目标点的距离距离
        graph = collections.defaultdict(list)
        for f, to, weight in times:
            graph[f].append((to, weight))

        # heap 记录 从起始节点start 到当前节点 cur 的最短距离
        # （start到当前节点最短距离，当前节点)。一开始初始化从最初起点出发，到自己节点的距离为0
        # 把距离放在前面是因为heaheap是根据第一个元素进行排序的
        heap = [(0, k)]

        # 从目标起点start出发到哪个节点: 最短距离。记录从初始节点到其他所有节点的最短距离
        # 初始化时都把距离设成正无穷
        dist = {k: 0}
        for to in range(1, n + 1):
            if to != k:
                dist[to] = float('inf')

        while heap:
            # 推出堆里从出发点到当前节点路径最短的点
            # 因为当这个from点更新完所有的相邻点后，则不再遍历这个节点了
            d1, cur = heapq.heappop(heap)

            # 从当前节点，遍历当前节点所能到达的所有节点
            for to, d2 in graph[cur]:
                # 假如 起始节点到当前节点的距离 + 当前节点的距离到下一个节点的距离 < 起始节点到下一个节点的距离
                # 那么更新 从起始节点到cur的下一个节点距离的最短路径值
                # 起到剪枝的效果，如果没有的话也可以运行成功，但会超时
                if d1 + d2 < dist[to]:
                    dist[to] = d1 + time
                    heapq.heappush(heap, (d1 + d2, to))

        # 看看能不能遍历完整个图，遍历不完的话说明不能使所有节点收到信号
        # 假如能遍历完的话，看到最远的节点需要多少时间，那就是需要多久才能使所有节点都收到信号
        res = max(dist.values())
        return res if res < float('inf') else -1
"""
time: E是times的长度，堆实现方式为O(ElogE),因为每个边都有可能被加进堆中
space: O(N+E) 图的大小是O(E) 加上其他对象的大小O(N)
"""
# 链接：https://leetcode-cn.com/problems/network-delay-time/solution/wang-luo-yan-chi-shi-jian-by-leetcode/

