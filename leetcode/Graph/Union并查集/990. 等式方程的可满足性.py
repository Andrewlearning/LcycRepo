class UF:
    parent = {}

    def __init__(self, equations):
        # 这里跟以往有点不一样，我们把两个元素互相指对方为父亲节点，构成 a == b的效果
        # 因为 a == b , b == c的话，我们要使 a,b,c都是联通的才行
        for eq in equations:
            self.parent[eq[0]] = eq[0]
            self.parent[eq[3]] = eq[3]

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, p, q):
        if self.connected(p, q):
            return
        self.parent[self.find(p)] = self.find(q)

    # 看两者的父亲节点是否一样，看是否联通
    def connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
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
https://leetcode-cn.com/problems/satisfiability-of-equality-equations/solution/mo-ban-ti-bing-cha-ji-python3-by-fe-lucifer/

并查集有一个重要的特征就是传导性，即A和B是连通的，B和C是连通的，那么A和C就是连通的。 是不是感觉和题目有点像？

题目中的 == 也一样具体传导性，因此我们的想法是基于 == 去 union 两个元素。 如果两个元素是连通的，并且 equation是 != 那么我们返回False，其他情况返回True
"""
