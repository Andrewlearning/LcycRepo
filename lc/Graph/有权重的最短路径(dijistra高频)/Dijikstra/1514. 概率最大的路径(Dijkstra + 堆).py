"""
给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成
，其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 w[i] 。

指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。

如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。
"""

class Solution(object):
    def maxProbability(self, n, edges, w, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type w: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        from collections import defaultdict
        import heapq
        graph = defaultdict(list)
        for i in range(len(edges)):
            f, to = edges[i]
            # 由于是无向图，所以两条边都要加
            graph[f].append([to, w[i]])
            graph[to].append([f, w[i]])

        # 因为我们要找概率最大的一条路线，所以得使用最大堆
        heap = [(-1.0, start)]

        # 从起点去其他点的最大可能性是多少
        # 初始化为最大可能性都为0，后面进行更新
        res = defaultdict(float)
        # 从起点到起点的可能性为1
        res[start] = 1.0

        while heap:

            # 推出最大可能性的节点
            d1, cur = heapq.heappop(heap)
            d1 *= -1.0

            # 假如我们已经记录一条路径的可能性比当前路径大
            # 那么则忽略这条路径
            if res[cur] > d1:
                continue

            # 查看当前节点相邻的所有节点
            for to, d2 in graph[cur]:
                # 从起点到当前节点的概率乘积
                newd = d1 * d2
                # 当前概率乘积 > 我们之前记录的从start -> to的最大概率乘积
                # 说明这条新路可以走
                if newd > res[to]:
                    # 更新从start -> to的最大概率乘积
                    res[to] = newd
                    heapq.heappush(heap, (-1.0 * newd, to))

        return res[end]