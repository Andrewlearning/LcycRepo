"""
给定员工的 schedule 列表，表示每个员工的工作时间。

每个员工都有一个非重叠的时间段 Intervals 列表，这些时间段已经排好序。

返回表示 所有 员工的 共同，正数长度的空闲时间 的有限时间段的列表，同样需要排好序。

示例 1：

输入：schedule = [
                [[1,2],[5,6]],
                [[1,3]],
                [[4,10]]
                ]
输出：[[3,4]]
解释：
共有 3 个员工，并且所有共同的
空间时间段是 [-inf, 1], [3, 4], [10, inf]。
我们去除所有包含 inf 的时间段，因为它们不是有限的时间段。
"""
"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""
import heapq
class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """

        res = []
        # 相当于按照会议开始时间来进行从小到大排序
        minheap = []
        for intervals in schedule:
            for interval in intervals:
                heapq.heappush(minheap, [interval.start, interval.end])
        cur = heapq.heappop(minheap)

        while minheap:

            # 假如说两个工作之间没有间隙，说明没有共同的休息时间，合并区间，再看下一个
            if cur[1] >= minheap[0][0]:
                # 那么我们就把工作的结束时间延长至最远
                cur[1] = max(cur[1], heapq.heappop(minheap)[1])

            # 假如两个工作之间有间隙，说明有共同的休息时间，记录
            # cur[1] < minheap[0][0]
            else:
                # 记录休息的间隙
                res.append([cur[1], minheap[0][0]])
                # 同时更新工作的时间
                cur = heapq.heappop(minheap)
        return res
