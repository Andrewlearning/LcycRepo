"""
输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3

"""
class UF:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0 for _ in range(n+1)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, p, q):
        proot, qroot = self.find(p), self.find(q)
        if proot == qroot:
            return
        if self.rank(proot) > self.rank(qroot):
            self.parent[qroot] = proot
        elif self.rank(proot) > self.rank(qroot):
            self.parent[proot] = qroot
        else:
            self.parent[proot] = qroot
            self.rank[proot] += 1


class Solution:
    def findRedundantConnection(self, edges):

        uf = UF(len(edges))
        for x,y in edges:

            # 我们发现两个点有共同的根节点，说明之前他们已经union过了，但是现在又出现一次
            # 说明这里出现重复了，返回
            if uf.find(x) == uf.find(y):
                return [x, y]
            else:
                uf.union(x, y)
        return []

"""
https://leetcode-cn.com/problems/redundant-connection/solution/bing-cha-ji-shui-ti-by-desgard_duan/
"""
