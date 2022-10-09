class UF:
    def __init__(self, M):
        self.parent = {}
        self.cnt = 0

        # 我们要理解，为什么这里self.parent只构造到n位
        # 因为这是本题的特性，因为例如本题的3*3 矩阵，其实这只有3个人
        n = len(M)
        for i in range(n):
            self.parent[i] = i
            # 我们每创建一个新的父亲，就把父亲的数量，self.cnt +1
            self.cnt += 1

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, p, q):
        if self.connected(p, q):
            return
        self.parent[self.find(p)] = self.find(q)
        # 我们找到两个最高节点，然后让一个指向另外一个，这个时候self.cnt -= 1
        # 父节点变小
        self.cnt -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

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
时间复杂度：O(n^3) 访问整个矩阵一次，并查集操作需要最坏O(n) 的时间。
空间复杂度：O(n)，parent 大小为 n。

https://leetcode-cn.com/problems/friend-circles/solution/mo-ban-ti-bing-cha-ji-python3-by-fe-lucifer-2/
"""