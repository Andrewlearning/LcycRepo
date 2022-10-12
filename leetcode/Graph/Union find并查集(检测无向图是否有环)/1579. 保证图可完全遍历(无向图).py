"""
lice 和 Bob 共有一个无向图，其中包含 n 个节点和 3 种类型的边：

类型 1：只能由 Alice 遍历。
类型 2：只能由 Bob 遍历。
类型 3：Alice 和 Bob 都可以遍历。

给你一个数组 edges ，其中 edges[i] = [typei, ui, vi]
表示节点 ui 和 vi 之间存在类型为 typei 的双向边。
请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。
如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。

返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。

输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
输出：2
解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。
再删除任何其他的边都无法保证图可以完全遍历。所以可以删除的最大边数是 2 。
"""
class UF:
    def __init__(self, M):
        # 每个点所能连接到的其他节点
        self.parent = {}
        # 一个图有对不同人有多少条可走路线
        self.cnt = 0

        # node从1开始
        n = M + 1
        for i in range(n):
            self.parent[i] = i

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)

        # 假如两个点都可以通往他们的父亲，且父亲相等，说明其中有重复的边，可以去掉一条边
        if fx == fy:
            return 1

        self.parent[fx] = fy
        # 说明这是一条有效的merge的边
        self.cnt += 1
        return 0

    def getCnt(self):
        return self.cnt

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # 两个人总共可以被删除的connection的数量
        res = 0
        # alice
        A = UF(n)
        # bob
        B = UF(n)

        # 该循环只连接A/B都可以走的的type3 connection
        for edge in edges:
            if edge[0] != 3:
                continue

            # 在这两个点之间画线，假如说这两个点祖先相等，那么说明这个线可以不用连接
            # 说明当前连接是重复的
            # res 只加一次就可以了，因为A 和 B此时是一摸一样的
            res += A.union(edge[1], edge[2])
            B.union(edge[1], edge[2])


        # 分别处理type1 type2
        for edge in edges:
            if edge[0] == 3:
                continue

            # 看当前处理的是Alice的图还是bob的图
            # 假如之前有edge 是 type3连接过了，说明这两个点没必要连，所以删边+1
            if edge[0] == 1:
                res += A.union(edge[1], edge[2])
            elif edge[0] == 2:
                res += B.union(edge[1], edge[2])

        # n个点应该最起码要有n-1条边相连
        if A.getCnt() == n - 1 and B.getCnt() == n - 1:
            return res
        return -1

# https://www.youtube.com/watch?v=eTQnRrmCWBc&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=2
