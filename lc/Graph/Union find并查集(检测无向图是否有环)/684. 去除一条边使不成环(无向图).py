"""
树可以看成是一个连通且 无环的无向图。

给定往一棵n 个节点 (节点值1～n) 的树中添加一条边后的图。
添加的边的两个顶点包含在 1 到 n中间，且这条附加的边不属于树中已存在的边。
图的信息记录于长度为 n 的二维数组 edges，edges[i] = [ai, bi]表示图中在 ai 和 bi 之间存在一条边。

请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。
如果有多个答案，则返回数组edges中最后出现的边。

n == edges.length

输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3

"""
class UF:
    def __init__(self, n):
        # 首先有多少个节点，那么就创建一个有多少个key-value对的字典
        # 节点值 ：父亲
        # 初始化是，每个节点的父亲都是自己
        self.parent = {}
        for i in range(1, n+1):
            self.parent[i] = i

    # union是，我们把两个节点的最父亲节点找到
    # 然后把其中一个节点的父亲指向另一个节点的父亲
    # 使得两个子树都有同样的父亲
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    # 最父亲节点的特征是：他的父亲也是自己
    # 所以我们要找到一个节点的最父亲节点，那么就是当 自己 != 父亲时
    # 父亲 = 父亲的父亲，这样一直找下去
    # 最后父亲节点就是最父亲节点
    # 同时这个函数，可以帮助一个节点直接连接上他的最父亲节点
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        uf = UF(n)

        # 我们发现两个点有共同的根节点，说明之前他们已经union过了，但是现在又出现一次
        for edge in edges:
            # 假如两个点已经有共同的根节点，且这两个节点目前已经有一条边了
            # 说明这里有环，那我们把这条边移除掉就满足题目要求了
            if uf.find(edge[0]) == uf.find(edge[1]):
                return edge
            uf.union(edge[0], edge[1])

        return []


"""
https://leetcode-cn.com/problems/redundant-connection/solution/bing-cha-ji-shui-ti-by-desgard_duan/
"""
