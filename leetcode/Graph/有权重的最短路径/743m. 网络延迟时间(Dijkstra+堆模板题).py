import heapq
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # 初始化图
        graph = collections.defaultdict(list)
        for cur, next, weight in times:
            graph[cur].append((next, weight))

        # （距离，哪个节点）
        pq = [(0, K)]
        #  哪个节点:距离, 记录从初始节点到其他所有节点的距离
        dist = {}

        while pq:
            # 推出堆里路径最短的点
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = d

            # 从当前节点，遍历当前节点的其他节点
            for nei, d2 in graph[node]:
                # 要是相邻节点已经被遍历过，说明相邻节点有更近的路到达，就不更新了
                # 否则则更新
                if nei not in dist:
                    # 把从开始节点到当前节点的所有路径给加进queue
                    heapq.heappush(pq, (d + d2, nei))

        # 看看能不能遍历完整个图，遍历不完的话说明不能使所有节点收到信号
        # 假如能遍历完的话，看到最远的节点需要多少时间，那就是需要多久才能使所有节点都收到信号
        return max(dist.values()) if len(dist) == N else -1
"""
time: E是times的长度，堆实现方式为O(ElogE),因为每个边都有可能被加进堆中
space: O(N+E) 图的大小是O(E) 加上其他对象的大小O(N)
"""
# 链接：https://leetcode-cn.com/problems/network-delay-time/solution/wang-luo-yan-chi-shi-jian-by-leetcode/

