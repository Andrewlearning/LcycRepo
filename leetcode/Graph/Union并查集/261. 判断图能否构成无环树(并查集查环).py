"""
请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。

示例 1：

输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
输出: true
示例 2:

输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
输出: false
"""

class Solution:
    def validTree(self, n, edges):
        # 如果边不等于顶点数减一， 则存在环
        if len(edges) != n - 1:
            return False

        # 并查集
        father = [i for i in range(n)]

        # 找到当前节点的最高节点
        def find(a):
            if a != father[a]:
                father[a] = find(father[a])
            return father[a]

        # 他所做的
        def union(a, b):
            father[find(b)] = find(a)

        # 把所有的边都指向同一个最高节点，
        for edge in edges:
            union(edge[0], edge[1])


        # 这里是什么意思？？？
        for i in range(n):
            find(i)

        # 最后
        return len(set(father)) == 1

"""
https://leetcode-cn.com/problems/graph-valid-tree/solution/shi-yong-bing-cha-ji-jie-jue-xing-shu-bu-duo-by-yi/

261，323这两题可以放在一起看
"""
