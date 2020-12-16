class Solution:
    def criticalConnections(self, n, connections):
        #构建图
        self.graph = dict()
        for i in range(n):
            self.graph[i] = dict()

        for s, v in connections:
            self.graph[s][v] = 1
            self.graph[v][s] = 1

        #无向图中找桥
        # 一个环中的最早时间戳，可用于环与环之间的确认
        self.low = [0 for i in range(n)]
        # 当前节点第一次被探索到的时间戳
        self.discover = [0 for i in range(n)]
        self.res = []

        self.dfs(0, -1, 1)
        return self.res

    def dfs(self, node, pre, time):
        # 探索到当前节点的时间
        self.discover[node] = time
        # 暂时把
        self.low[node] = time

        for nextnode in self.graph[node]:
            # 如果该子节点不为父节点且未被访问过，即未被初始化时间戳
            if nextnode != pre and self.discover[nextnode] == 0:
                # 递归，探索下一个节点
                self.dfs(nextnode, node, time + 1)

                # 如果子节点最早时间戳仍大于当前节点的时间戳
                # 说明当前节点和子节点不在同一个环上
                # 那么他们两之间的边就是桥
                if self.discover[node] < self.low[nextnode]:
                    self.res.append([node, nextnode])

                # 更新当前节点的最早时间
                self.low[node] = min(self.low[node], self.low[nextnode])

            # 如果存在已访问的子节点，说明构成一个环了
            # 跟他比较更新自己的最小时间戳
            elif nextnode != pre and self.discover[nextnode] != 0:
                self.low[node] = min(self.low[node], self.low[nextnode])

"""
Solution: Tarjan，来自huahua
Time complexity: O(v+e)
Space complexity: O(v+e)

Tarjan求出无向图的割点与桥，进一步地可以求解无向图的双连通分量；
同时，也可以求解有向图的强连通分量、必经点与必经边。
代码：https://leetcode-cn.com/problems/critical-connections-in-a-network/solution/python-ji-yu-tarjansuan-fa-de-wu-xiang-tu-zhong-zh/
思路：https://www.bilibili.com/video/BV15t4y197eq/

"""


