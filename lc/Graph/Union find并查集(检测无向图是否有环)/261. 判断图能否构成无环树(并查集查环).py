"""
请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。

示例 1：

输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
输出: true
示例 2:

输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
输出: false
"""
class UF:
    def __init__(self, n):
        self.parent = {}
        self.cnt = 0
        for i in range(n):
            self.parent[i] = i
            self.cnt += 1

    # 本题在这有特殊的判断逻辑
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        # 假如我们输入的两个节点是属于同一个父亲，那么他们相连会形成环，不满足题目条件
        if fx == fy:
            return False
        self.parent[fx] = self.find(fy)
        self.cnt -= 1
        return True

    # path compression写法
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # 构造uf
        uf = UF(n)

        # 把所有的节点都union起来
        # 假如有节点在union之前，就已经归属于同一个父节点下了，说明这样一连会形成环，无法够成树
        for edge in edges:
            if uf.union(edge[0], edge[1]) is False:
                return False

        # 最后看最父亲节点是不是只有一个，只有一个则说明不会成环，可以构成树
        return uf.cnt == 1
"""
Tree vs Graph
A tree is a special undirected graph. It satisfies two properties
- It is connected
- It has no cycle.

261，323这两题可以放在一起看
https://blog.csdn.net/hgq522/article/details/121690420
"""
