"""
给定编号从 0 到 n-1 的 n 个节点和一个无向边列表（每条边都是一对节点），
请编写一个函数来计算无向图中连通分量的数目。

示例 1:

输入: n = 5 和 edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

输出: 2

翻译年糕： 这个图里面总共有多少个不同的 父亲， 有多少个不同的连通分量
"""
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        # 一开始有n个各自为政的连通分量，他们都指向自己
        self.cnt = n


    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        # 假如已经同属于一个连通分量了，就不用进行连接了，跳过
        if fx == fy:
            return
        # 每合并一次，就说明连通分量少了一个
        self.parent[fx] = fy
        self.cnt -= 1


class Solution(object):
    def countComponents(self, n, edges):
        uf = UF(n)

        for e1, e2 in edges:
            uf.union(e1, e2)

        # 最后返回连通分量的数量就好了
        return uf.cnt