"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
return the maximum number of points that lie on the same straight line.

Input: points = [[1,1],[2,2],[3,3]]
Output: 3
解释： [1,1],[2,2],[3,3] 在同一条直线上

Input: points = [[1,1],[5,3],[3,2],[4,1],[2,3],[1,4]]
Output: 4
解释： [3,2],[4,1],[2,3],[1,4] 在同一条直线上
"""

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        # 两点之间必有一条直线，所以这一条直线最多可以穿过两个点
        if len(points) < 3:
            return len(points)

        res = 0
        n = len(points)

        for i in range(n):
            # key：斜率， value：除i节点外，还有多少个节点在这条i所在的斜率为k的线上
            m = defaultdict(int)
            # overlap = 0  # 记录与当前点重合的点数量。当前题目不要求这个情况，不存在相同点的情况
            vertical = 0  # 记录与当前点垂直的点数量
            localMax = 0

            for j in range(n):
                # 不用计算自己与自己这种情况
                if i == j:
                    continue

                x = points[i]
                y = points[j]

                # 假如两个节点的y值相同，则说明在一条垂线上
                # 由于垂线的分母为 y1 - y2 = 0 / x1 - x2 = 0, 无法相除, 所以通过这种方式记录
                if x[0] == y[0]:
                    # if x[1] == y[1]:
                    #     overlap += 1
                    # else:
                    vertical += 1
                else:
                    # 计算斜率k, 看有多少个点和当前i节点的斜率相同，斜率相同且经过i点，则说明与i点在同一条直线上
                    k = float(y[1] - x[1]) / float(y[0] - x[0])
                    m[k] += 1
                    # 记录有最多有多少个节点 与 i节点在同一条直线上
                    localMax = max(localMax, m[k])

            # localMax + 1, 最多节点在的一条线 + 自己这个节点
            # vertical + 1，多少个节点在垂线 + 自己这个节点
            res = max(res, localMax + 1, vertical + 1)

        return res

"""
来源自 https://www.acwing.com/video/1520/
"""