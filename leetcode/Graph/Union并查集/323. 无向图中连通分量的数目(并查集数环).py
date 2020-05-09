"""
给定编号从 0 到 n-1 的 n 个节点和一个无向边列表（每条边都是一对节点），请编写一个函数来计算无向图中连通分量的数目。

示例 1:

输入: n = 5 和 edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

输出: 2

翻译年糕： 这个图里面总共有多少个不同的 父亲， 有多少个不同的集合
"""


class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    # 当一个node 不是指向自己的时候，那么它就要一直向上找，直到找到自己的父亲
    def find(self, x):
        if x != self.parent[a]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # union这里，谁的做谁的父亲问题都不大，有涌向的可能就是效率问题
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return

        self.parent[proot] = qroot


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UF(n)

        # 把所有的边都指向同一个最高节点，
        for e1, e2 in edges:
            uf.union(e1, e2)

        #
        for i in range(n):
            uf.find(i)

        return len(set(uf.parent))

"""
261，323这两题可以放在一起看
"""