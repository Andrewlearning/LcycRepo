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
        # 首先有多少个节点，那么就创建一个有多少个key-value对的字典
        # 节点值 ：父亲
        # 初始化是，每个节点的福清都是自己
        self.parent = {}
        for i in range(n):
            self.parent[i] = i

    # union是，我们把两个节点的最父亲节点找到
    # 然后把其中一个节点的父亲指向另一个节点的父亲
    # 使得两个子树都有同样的父亲
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

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
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # 构造uf
        uf = UF(n)

        # 把每个子节点都指向他的父亲节点
        for edge in edges:
            uf.union(edge[0], edge[1])

        # 我们把每个节点都指向他的最父亲节点
        for i in range(n):
            uf.find(i)

        res = set(uf.parent.values())

        # 最后看最父亲节点有几个
        return len(res)

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