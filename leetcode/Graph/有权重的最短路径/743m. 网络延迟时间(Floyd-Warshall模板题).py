class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # 初始化：最开始任意两点的距离都设置为最大值
        # 记录两个节点之间的最小距离
        graph = [[float("inf")] * (N + 1) for _ in range(N + 1)]
        # 因为是有向图，所以只设置单向的距离
        for i, j, t in times:
            graph[i][j] = t

        # 该层循环为(i, j)路径的各个中间跳节点
        for k in range(1, N + 1):
            # 该层循环为(i, j)路径的各个u节点
            for i in range(1, N + 1):
                # 该层循环为(i, j)路径的各个v节点
                for j in range(1, N + 1):
                    # 如果(i, j)路径的花费比借助k节点跳跃的路径(即先(i, k)，再(k, j))花费更少，则更新(i, j)的最小花费
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        max_time = 0
        # 遍历各个节点：选出节点K到所有节点的最大花费，即为整个网络的最大花费。
        for i in range(1, N + 1):
            if i != K:
                max_time = max(max_time, graph[K][i])

        # 需要判断是否网络不通
        return -1 if max_time == float("inf") else max_time

"""
Time complexity: O(n^3)
Space complexity: O(n^2)

https://leetcode-cn.com/problems/network-delay-time/solution/biao-zhun-de-floydsuan-fa-xiang-jie-by-tunsuy/
"""
