class UF:
    def __init__(self):
        self.parent = {}

    # 假如x没有parent的话，那么就把parent指向自己
    def initParent(self, x):
        if x not in self.parent:
            self.parent[x] = x

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        self.parent[fx] = fy


class Solution:
    def accountsMerge(self, accounts):
        import collections
        uf = UF()
        # 每个email 与这个 email对应的用户名字
        emailToName = {}
        # keys: 同属于一个union的emails的根节点(email)
        # values: 同属于一个union的emails list
        rootMap = collections.defaultdict(list)

        for account in accounts:
            for i in range(1, len(account)):
                name = account[0]
                email = account[i]
                if email not in emailToName:
                    emailToName[email] = name

                # 初始化当前邮箱的parent
                uf.initParent(account[i])

                # 假如这个人拥有>1的邮箱账号，那就把这些邮箱账号union起来
                # 使得同一个人的所有账号都是同一个父亲
                if i > 1:
                    uf.union(account[i - 1], account[i])

        # 我们把属于同一个人的email都加到一个list里
        for email in emailToName:
            rootEmail = uf.find(email)
            rootMap[rootEmail].append(email)
        
        res = []
        for emails in rootMap.values():
            name = [emailToName[emails[0]]]
            res.append(name + sorted(emails))
        return res
