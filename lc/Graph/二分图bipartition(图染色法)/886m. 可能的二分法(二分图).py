class Solution:
    def dfs(self, cur, color, N):

        # 首先先对当前老哥上色
        self.colors[cur] = color

        # 获得当前节点的邻居
        for neigh in self.graph[cur]:
            # 假如这个邻居跟当前老哥同色的话，说明是错的
            if self.colors[neigh] == color:
                return False
            # 假如邻居没上过色，然后就对邻居上色， 没出问题的话就过了
            if self.colors[neigh] == 0 and not self.dfs(neigh, -1 * color, N):
                return False

        return True

    def possibleBipartition(self, N, dislikes):
        # 表面点与点之间是否相邻
        self.graph = [[] for i in range(N)]
        # 记录颜色关系
        self.colors = [0] * N

        # 记录邻居
        for a, b in dislikes:
            self.graph[a - 1].append(b - 1)
            self.graph[b - 1].append(a - 1)

        # 0-未到访过，1-红色，-1-蓝色
        # 遍历途中未被标记的人，从他们开始做dfs
        for i in range(N):
            if self.colors[i] == 0 and not self.dfs(i, 1, N):
                return False

        return True


# 作者：fe-lucifer
# 链接：https://leetcode-cn.com/problems/possible-bipartition/solution/ran-se-fa-er-fen-tu-886-ke-neng-de-er-fen-fa-by-fe/



import collections
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        self.graph = collections.defaultdict(list)

        # 给能联通的节点相互赋值
        for u, v in dislikes:
            self.graph[u].append(v)
            self.graph[v].append(u)

        # 记录每个节点的染色情况
        self.color = {}

        res = []
        # 我们的node的范围是[1,N]
        for node in range(1, N + 1):
            if node not in self.color:
                res.append(self.dfs(node, 0))

        return all(res)

    def dfs(self, node, c):
        # 假如node的颜色已经被记录过，查看是否有冲突，有冲突的话返回False
        if node in self.color:
            return self.color[node] == c

        # 染色当前节点
        self.color[node] = c

        # 把所有联通的节点都跑一边，完成染色，同时记录是否有冲突
        return all(self.dfs(neighbour, c ^ 1) for neighbour in self.graph[node])


# 时间复杂度(N+E)，其中 E 是 dislikes 的长度
# 空间复杂度O(N+E)
# 链接：https://leetcode-cn.com/problems/possible-bipartition/solution/ke-neng-de-er-fen-fa-by-leetcode/

