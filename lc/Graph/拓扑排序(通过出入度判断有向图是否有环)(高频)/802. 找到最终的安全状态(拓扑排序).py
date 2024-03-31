"""
每个列表里面，代表i下一步能去的节点
那些不会构成死循环的点，就是安全的点

示例：
输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
输出：[2,4,5,6]
解释：示意图如上。
节点 5 和节点 6 是终端节点，因为它们都没有出边。
从节点 2、4、5 和 6 开始的所有路径都指向节点 5 或 6 。

反例: 0 - 1 - 3 - 0 这样会构成一个环
"""
class Solution(object):
    def eventualSafeNodes(self, g):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        n = len(g)
        safe = [False] * n

        # 下一个节点 -> [前一个节点1，前一个节点2]
        # next -> cur
        graph = defaultdict(list)
        # 每一个节点有多少个指向其他节点的边(出度) cur -> next
        outdegree = defaultdict(int)
        for i in range(n):
            for next in g[i]:
                cur = i
                graph[next].append(cur)
                outdegree[cur] += 1

        # 收集出度为0的节点，这些节点是第一批安全的节点
        queue = []
        for node in range(n):
            if outdegree[node] == 0:
                queue.append(node)

        while queue:
            # 把出度为0的节点pop出来，因为出度为0代表着不会构成死循环，所以是安全的
            cur = queue.pop(0)
            # 记录这个安全的点
            safe[cur] = True

            # 遍历cur前面的节点
            for pre in graph[cur]:

                # 把cur前面的节点的出度都-1， 因为cur已经被删除了
                outdegree[pre] -= 1

                # 看看cur前面的节点有没有出度为0的，有的话加进queue
                # 因为和安全节点相连的节点，也是安全的
                if outdegree[pre] == 0:
                    queue.append(pre)

        # 我们要按顺序输出安全节点
        return [i for i in range(n) if safe[i]]

"""
https://www.acwing.com/activity/content/problem/content/3820/
如果一个点，出度为0的话，那说明这个点到不了其他点上，这必然是一个安全的点
如果一个点，出边所对应所有的点，都是安全的，那它是安全的

如果一个点，可以到一个不安全的点，那说明这个点也是不安全的
"""