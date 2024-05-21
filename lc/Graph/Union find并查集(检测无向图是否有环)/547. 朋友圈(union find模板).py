"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，
且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，
其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连
而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
"""
class UF:
    def __init__(self, M):
        # key:child, value:parent
        self.parent = {}
        self.cnt = 0

        # 我们要理解，为什么这里self.parent只构造到n位
        # 因为题目说的有 n 个城市
        n = len(M)
        for i in range(n):
            self.parent[i] = i
            # 我们每创建一个新的父亲，就把父亲的数量，self.cnt +1
            self.cnt += 1

    # 使用了path compression
    # 会把从x到最终parent一条路上的所有节点都指向最高的parent
    # time: O(n), 主要为find的时间, 最差情况下为n, 但但凡遍历过一次就变为O(1)
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # time: O(n), 主要为find的时间
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx == fy:
            return
        # 我们找到两个最高节点，然后让一个指向另外一个，这个时候self.cnt -= 1
        # 父节点变小
        self.parent[fx] = fy
        self.cnt -= 1

class Solution:
    def findCircleNum(self, M):
        n = len(M)

        uf = UF(M)
        for i in range(n):
            for j in range(n):
                # [i][j] == 1, 那就说 i,j有朋友关系，意思就是他们共属于同一个父亲
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.cnt


"""
时间复杂度：O(n^2) 访问整个矩阵一次，并查集操作需要最坏O(n) 的时间。
空间复杂度：O(n)，parent 大小为 n。
"""