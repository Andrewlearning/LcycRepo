class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        maxTime = float("inf")
        # 设定从起点到当前点的距离都是为inf
        dist = [maxTime] * (N+1)
        # 从自己到自己的距离为0
        dist[K] = 0

        # 有N个节点，所有遍历N次
        for i in range(N):
            # 每次遍历都会重新动态规划所有times,更新所有的距离关系
            for time in times:
                frm = time[0]
                to = time[1]
                weight = time[2]
                dist[to] = min(dist[to], dist[frm] + weight)

        # 第一个节点没用上,pop掉
        dist.pop(0)
        # 看在这个图里最耗时间是需要多久
        maxDist = max(dist)

        # 假如所有图都有遍历到，说明解释成立的，则返回最大耗时
        return -1 if maxDist == maxTime else maxDist

"""
Time complexity: O(ne)
Space complexity: O(n)
https://zxi.mytechroad.com/blog/graph/leetcode-743-network-delay-time/
"""