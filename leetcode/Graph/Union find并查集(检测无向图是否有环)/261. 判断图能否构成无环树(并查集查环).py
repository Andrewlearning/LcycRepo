"""
请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。

示例 1：

输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
输出: true
示例 2:

输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
输出: false
"""
# 用这种写法比较好
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
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # 如果边不等于顶点数减一， 则存在环
        if len(edges) != n - 1:
            return False

        # 构造uf
        uf = UF(n)

        # 把每个子节点都指向他的父亲节点
        for edge in edges:
            uf.union(edge[0], edge[1])

        # 我们把每个节点都指向他的最父亲节点
        for i in range(n):
            uf.find(i)

        res = set(uf.parent.values())

        # 最后看最父亲节点是不是只有一个
        return len(res) == 1
"""
https://leetcode-cn.com/problems/graph-valid-tree/solution/shi-yong-bing-cha-ji-jie-jue-xing-shu-bu-duo-by-yi/

261，323这两题可以放在一起看
"""
