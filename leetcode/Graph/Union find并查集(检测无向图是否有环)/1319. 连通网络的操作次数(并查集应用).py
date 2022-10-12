"""
输入：n = 4, connections = [[0,1],[0,2],[1,2]]
输出：1
解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。

"""
class UF:
    def __init__(self, n):
        self.parent = {}
        # 表示当前有多少个连通分量
        self.count = n
        for i in range(n):
            self.parent[i] = i

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx == fy:
            return

        self.parent[self.find(fx)] = self.find(fy)
        # 每连接两个联通分量，那么图里连接的线就 -= 1
        self.count -= 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def getCount(self):
        return self.count


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        uf = UF(n)

        # 查看有多少线是多余的，同时也代表着合并的次数
        dupCnt = 0
        for x, y in connections:
            fx, fy = uf.find(x), uf.find(y)
            # 假如一个connection的两个点的父亲节点一样
            # 说明这条线是冗余的线，可以去掉
            if fx == fy:
                dupCnt += 1
            # 然后连接
            uf.union(x, y)


        # 获得有多少个没有相互连接的连通分量getCount，其中这些联通分量需要getCount - 1次连接
        # 才能使得所有计算机都连接起来
        needConnet = uf.getCount() - 1

        # 假如多余的连接 < 需要的连接，说明无法把所有的计算机连接起来
        if dupCnt < needConnet:
            return -1
        else:
            return needConnet
