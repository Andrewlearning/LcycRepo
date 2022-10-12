"""
在一个社交圈子当中，有N个人。每个人都有一个从0 到N-1唯一的 id编号。

我们有一份日志列表logs，其中每条记录都包含一个非负整数的时间戳
以及分属两个人的不同id，logs[i] = [timestamp, id_A, id_B]。

每条日志标识出两个人成为好友的时间，友谊是相互的
：如果 A 和 B 是好友，那么 B 和 A 也是好友。

如果 A 是 B 的好友，或者 A 是 B 的好友的好友
那么就可以认为 A 也与 B 熟识。

返回圈子里所有人之间都熟识的最早时间。如果找不到最早时间，就返回 -1 。


示例：

输入：logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], N = 6
输出：20190301
解释：
第一次结交发生在 timestamp = 20190101，0 和 1 成为好友，社交朋友圈如下 [0,1], [2], [3], [4], [5]。
第二次结交发生在 timestamp = 20190104，3 和 4 成为好友，社交朋友圈如下 [0,1], [2], [3,4], [5].
第三次结交发生在 timestamp = 20190107，2 和 3 成为好友，社交朋友圈如下 [0,1], [2,3,4], [5].
第四次结交发生在 timestamp = 20190211，1 和 5 成为好友，社交朋友圈如下 [0,1,5], [2,3,4].
第五次结交发生在 timestamp = 20190224，2 和 4 已经是好友了。但是社交圈还是没变
第六次结交发生在 timestamp = 20190301，0 和 3 成为好友，大家都互相熟识了。
假如说后续还有结交，但是我们所需要获得的结交就停留在这里了，因为这是最早让大家都成为朋友的时间点

"""

class UF:
    def __init__(self, N):
        # amount表示 当前union里有几个元素，初始化都为1
        self.amount = [1] * N
        self.parent = [i for i in range(N)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        self.parent[fx] = fy
        # 在union完后，往最终父亲方加上新合进来union的元素数量
        self.amount[fy] += self.amount[fx]


class Solution:
    def earliestAcq(self, logs, N):
        uf = UF(N)

        # 因为logs第一个元素是时间，所以我们先对时间进行一个排序
        # 因为朋友圈的形成是按照时间点的顺序来发生的
        logs.sort()

        for time, a, b in logs:

            # 每次让a,b所属的朋友圈结交一下
            uf.union(a, b)

            # 这里find(a) 或是(b)都没关系，因为他们已经成为一个朋友圈
            # 所以这两个点向上找都肯定会找到同一个root
            # 并且这个root已经被我们处理过， a,b两个朋友圈的人数早已复制到amount[root]里去了
            if uf.amount[uf.find(a)] == N:
                return time

        return -1