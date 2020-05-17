class UF:
    def __init__(self):
        # 因为这里处理的不再是数字了，所以我们用字典来表示父子关系
        self.parent = {}

    def find(self, x):
        # 在这里先进行一次初始化，把元素的父亲指向自己
        self.parent.setdefault(x, x)
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return

        self.parent[proot] = qroot


class Solution:
    def accountsMerge(self, accounts):
        uf = UF()
        email_to_name = {}
        res = collections.defaultdict(list)

        for account in accounts:
            for i in range(1, len(account)):
                email_to_name[account[i]] = account[0]
                if i < len(account) - 1:
                    uf.union(account[i], account[i + 1])

        for email in email_to_name:
            res[uf.find(email)].append(email)

        return [[email_to_name[value[0]]] + sorted(value) for value in res.values()]
