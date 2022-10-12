"""
给定一个由表示变量之间关系的字符串方程组成的数组，
每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或"a!=b"。
在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回true，否则返回 false。

输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。

输入：["b==a","a==b"]
输出：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
"""
class UF:
    def __init__(self, equations):
        self.parent = {}

        # 初始化每个节点的parent
        for eq in equations:
            self.parent[eq[0]] = eq[0]
            self.parent[eq[3]] = eq[3]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    # 看两者的父亲节点是否一样
    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def equationsPossible(self, equations):
        uf = UF(equations)

        # a == b, 把a,b 连到同一个父亲节点里去
        for eq in equations:
            if eq[1] == '=':
                uf.union(eq[0], eq[3])

        # a != b, 那么检查，假如说发现 a,b有同一个父亲节点，说明 a == b,冲突
        # 返回False
        for eq in equations:
            if eq[1] == '!' and uf.connected(eq[0], eq[3]):
                return False
        return True

"""
时间复杂度：平均 O(logN)O(logN)，最坏的情况是 O(N)
空间复杂度：我们使用了 parent， 因此空间复杂度为 O(N)
"""
