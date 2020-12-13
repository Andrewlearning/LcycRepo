"""
对于一个具有树特征的无向图，我们可选择任何一个节点作为根。
图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。
给出这样的一个图，写出一个函数找到所有的最小高度树并返回他们的根节点。

格式
该图包含 n 个节点，标记为 0 到 n - 1。
给定数字 n 和一个无向边 edges 列表（每一个边都是一对标签）。
你可以假设没有重复的边会出现在 edges 中。
由于所有的边都是无向边， [0, 1]和 [1, 0] 是相同的，因此不会同时出现在 edges 里。
示例 1:
输入: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

输出: [1]
"""
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        adj = [set() for i in range(n)]

        # 把彼此作为相邻节点都加进列表里
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        # 只有一个相连节点的 节点，一定为叶子节点
        leaves = [i for i in range(len(adj)) if len(adj[i]) == 1]

        # 我们要做的是，把连接节点从少到多的顺序删，因为连接节点少的点，代表着它很边缘，相对应来说就是以他
        # 做root.树会很高
        # 删到最后的节点的时候，说明那就是最中心的节点，意味着最矮
        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for i in leaves:
                # x元素在leaves
                # 首先把x的set里的元素清空
                j = adj[i].pop()
                # 其次再把拥有 x这个元素的set中,删掉x
                adj[j].remove(i)
                # 然后看这个拥有 x这个元素的set,的长度
                # 假如长度为1的话，有可能是下一轮处理，也有可能这就是答案
                if len(adj[j]) == 1:
                    new_leaves.append(j)

            leaves = new_leaves

        return leaves
"""
思路：
https://algocasts.io/episodes/AwmXLzmx
https://www.youtube.com/watch?v=pUtxTz134qM
代码：https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
答案：
这里涉及到一个图的理论， 假如说你不知道的话这题是没办法做出来的（收缩法）
1.我们要不断删除，连接点只有1的点，删除到最后余下的点，都是长度最小的点
2.做法比较取巧
"""