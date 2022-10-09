"""
输入：n = 4, connections = [[0,1],[0,2],[1,2]]
输出：1
解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。

"""
class UF:
    def __init__(self, n):
        self.parent = {}
        self.count = n
        for i in range(n):
            self.parent[i] = i

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return

        self.parent[self.find(rootX)] = self.find(rootY)
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
        numCut = 0
        for x, y in connections:
            x_, y_ = uf.find(x), uf.find(y)
            # 发现冗余的线，可以去掉
            if x_ == y_:
                numCut += 1
            # 然后连接
            uf.union(x, y)

        # n台电脑总共需要合并n-1次
        # 如果已经合并了numCut次,则还需合并n-1-numCut次
        needConnet = uf.getCount() - 1
        if numCut < needConnet:
            return -1
        else:
            return needConnet
