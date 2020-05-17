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

        # 把两个节点的父节点连起来
        for e1, e2 in edges:
            uf.union(e1, e2)

        # 这里是最关键的一步，很多节点只是联通在一起了，但是不代表
        # 他们指向向的是同一个根节点，所以最后我们还是要全部节点找一次最父节点
        for i in range(n):
            uf.find(i)

        return len(set(uf.parent))

"""
261，323这两题可以放在一起看

上面那种写法比较粗鄙，但是可以帮助我们理解union find 的内核
下面这种用了一种比较通用的求解联通分量数量的方法，做法与500是一致的
"""


class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        # 一开始有n个各自为政的联通分量，他们都指向自己
        self.cnt = n


    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    # 每合并一次，就说明联通分量少了一个
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return

        self.parent[proot] = qroot
        self.cnt -= 1


class Solution(object):
    def countComponents(self, n, edges):
        uf = UF(n)


        for e1, e2 in edges:
            uf.union(e1, e2)

        # 最后返回联通分量就好了
        return uf.cnt