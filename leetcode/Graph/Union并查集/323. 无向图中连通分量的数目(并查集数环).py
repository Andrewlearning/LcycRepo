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


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        # 并查集
        father = [i for i in range(n)]

        # 找到当前节点的最高节点
        def find(a):
            if a != father[a]:
                father[a] = find(father[a])
            return father[a]

        # 他所做的就是把找到他们的父亲，并把父亲进行一个指向
        def union(a, b):
            father[find(b)] = find(a)

        # 把所有的边都指向同一个最高节点
        for edge in edges:
            union(edge[0], edge[1])

        # 最后把所有的节点的再指向一次自己的最高父亲
        for i in range(n):
            find(i)

        return len(set(father))

"""
261，323这两题可以放在一起看
"""