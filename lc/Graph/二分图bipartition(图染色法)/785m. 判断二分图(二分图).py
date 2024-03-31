"""
给定一个无向图graph，当这个图为二分图时返回true。

如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释:
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。
"""

class Solution:
    def dfs(self, cur, color, N):
        # 对当前点上色
        self.colors[cur] = color

        # 找当前点的邻居
        for j in range(N):
            if self.graph[cur][j] == 1:
                # 发现邻居跟自己一样颜色，那么错了
                if self.colors[j] == color:
                    return False
                # 邻居没上过色，那么就去上色
                if self.colors[j] == 0 and not self.dfs(j, -1 * color, N):
                    return False
        return True

    def isBipartite(self, graph):
        N = len(graph)
        # 点与点之间的关系
        self.graph = [[0] * N for _ in range(N)]
        # 每个点的颜色
        self.colors = [0] * N

        # 初始化点与点之间的关系
        # [i][j]两点要是想连，那么[i][j] = 1
        for i in range(N):
            for j in graph[i]:
                self.graph[i][j] = 1

        # 0-未到访过，1-红色，-1-蓝色
        # 遍历途中未被标记的人，从他们开始做dfs
        for i in range(N):
            if self.colors[i] == 0 and not self.dfs(i, 1, N):
                return False

        return True

# 作者：fe-lucifer
# 链接：https://leetcode-cn.com/problems/is-graph-bipartite/solution/ran-se-fa-dfs-he-886-ke-neng-de-er-fen-fa-yi-ge-ta/