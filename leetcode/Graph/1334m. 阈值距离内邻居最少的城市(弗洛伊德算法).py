"""
输入：n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
输出：3
解释：城市分布图如上。
每个城市阈值距离 distanceThreshold = 4 内的邻居城市分别是：
城市 0 -> [城市 1, 城市 2]
城市 1 -> [城市 0, 城市 2, 城市 3]
城市 2 -> [城市 0, 城市 1, 城市 3]
城市 3 -> [城市 1, 城市 2]
城市 0 和 3 在阈值距离 4 以内都有 2 个邻居城市，但是我们必须返回城市 3，因为它的编号最大。
"""

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        if not edges:
            return 0

        # 初始化：最开始任意两点的距离都设置为最大值
        edges_map = [[10001 for _ in range(n)] for _ in range(n)]

        # 注意：这里是无向图
        for i, j, dist in edges:
            edges_map[i][j] = dist
            edges_map[j][i] = dist

        # 计数任意两个点的最短距离
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    edges_map[i][j] = min(edges_map[i][j],
                                          edges_map[i][k] + edges_map[k][j])

        res = 0
        min_count = float("inf")
        # 计算任意两个点最短距离满足题目要求的点
        for _from in range(n):
            count = 0
            # 从from点出发，到任意一个点距离小于阈值的个数
            for _to in range(n):
                if _from != _to and edges_map[_from][_to] <= distanceThreshold:
                    count += 1

            # 更新这个能到达城市的最小值
            if count <= min_count:
                min_count = count
                res = _from

        return res