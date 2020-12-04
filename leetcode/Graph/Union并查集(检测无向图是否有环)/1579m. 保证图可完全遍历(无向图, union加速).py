"""
lice 和 Bob 共有一个无向图，其中包含 n 个节点和 3 种类型的边：

类型 1：只能由 Alice 遍历。
类型 2：只能由 Bob 遍历。
类型 3：Alice 和 Bob 都可以遍历。
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
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, p, q):
        findP = self.find(p)
        findQ = self.find(q)

        # 假如两个点都可以通往他们的父亲，且父亲相等，说明其中有重复的边，可以去掉一条边
        if findP == findQ:
            return 1

        # 加速，找到统一祖先，避免过度调用find()
        maxParent = max(p, q, findP, findQ)

        # 合并
        self.parent[findP] = maxParent
        self.parent[findQ] = maxParent
        self.parent[p] = maxParent
        self.parent[q] = maxParent

        # 说明这是一条有效的merge的边
        self.cnt += 1
        return 0

    def edges(self):
        return self.cnt


import copy


class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        res = 0
        # alice
        A = UF(n)

        # 该循环只画出必要的type3
        for edge in edges:
            # 当前只处理type3的情况
            if edge[0] != 3:
                continue

            # 在这两个点之间画线，假如说这两个点祖先相等，那么说明这个线可以不用画，是重复的
            # 因为通过即使不画这个线，这两个点也能走到一起
            # 只加一次就可以了，因为A 和 B此时是一摸一样的
            res += A.union(edge[1], edge[2])

        # 因为第三条边alice 和 bob都可以走，所以他们两的图应该是一样的
        # bob
        B = copy.deepcopy(A)

        # 分情况处理type1 type2
        for edge in edges:
            if edge[0] == 3:
                continue

            # 看当前处理的是Alice的图还是bob的图
            # 假如之前有type3连接过了，说明这两个点没必要连，所以删边+1
            if edge[0] == 1:
                res += A.union(edge[1], edge[2])
            elif edge[0] == 2:
                res += B.union(edge[1], edge[2])

        # n个点应该最起码要有n-1条边相连
        if A.edges() == n - 1 and B.edges() == n - 1:
            return res
        return -1

# https://www.youtube.com/watch?v=eTQnRrmCWBc&list=PLLuMmzMTgVK5gFVMpryw0LkJp4l9WTtdM&index=2
