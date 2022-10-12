# coding:utf-8
class UnionFind(object):
    def __init__(self, n):
        self.parent = {}
        for i in range(n):
            self.parent[i] = i

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x1, x2):
        root1 = self.find(x1)
        root2 = self.find(x2)
        # 要合并，retunr false
        if root1 != root2:
            self.parent[root2] = root1
            return False
        # 父亲一样，不合并，return True
        return True

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        uf = UnionFind(n + 1)

        # 记录最后一条重复的边
        last = []
        parent = {}
        candidates = []
        for st, ed in edges:

            # 当前节点已经有父亲了，说明此时有两个点指向ed
            if ed in parent:
                candidates.append([parent[ed], ed])
                candidates.append([st, ed])
            # 当前节点没父亲，说明是一条单向的线
            else:
                parent[ed] = st
                # 当发现st,ed早已在同一个联通分路的时候，我们要记录当前这个多连的边
                if uf.union(st, ed):
                    last = [st, ed]

        # 情况1，度都为1，找出重复链接的边
        if not candidates:
            return last

        # 情况3，存在度为2的边，且之前在遍历度为1的时候发生过重复，那么删掉度1重复的
        if last:
            candidates[0]

        # 情况2，不存在度为2的边，且之前在遍历度为1的时候没有重复，那么删掉度2后来的边
        return candidates[1]


"""
视频思路：理解三种情况
https://www.bilibili.com/video/BV13t41157K5?from=search&seid=1317598284124498974

文字思路：
1. 都是度为1， 则找出构成环的最后一条边
2. 有度为2的两条边(A->B, C->B)，则删除的边一定是在其中
    先不将C->B加入并查集中，若不能构成环，则C->B是需要删除的点边，
    反之，则A->B是删除的边(去掉C->B还能构成环，则C->B一定不是要删除的边)

所以分为三个情况：
情况1：都是度为1， 则找出构成环的最后一条边
情况2：遍历到有度为2的两条边，假如说，在遍历度为1的边的时候，已经发现了重复，那么删除度为2且在之前已经重复的边
情况3：遍历到有度为2的两条边，假如说，在遍历度为1的边的时候，已经发现了重复，那么最后构成度为2的边是导致重复的边

链接：https://leetcode-cn.com/problems/redundant-connection-ii/solution/python-jian-ji-dai-ma-bing-cha-ji-de-yun-yong-by-y/

"""