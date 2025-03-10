"""
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，
为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:

输入: [[0, 30],[5, 10],[15, 20]]
输出: 2
"""
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        points = []
        for interval in intervals:
            # [会议开始时间,1]，1表示记录这个房间
            # [会议结束时间,-1] -1取消对这个房间的追踪
            points.append((interval[0], 1))
            points.append((interval[1], -1))

        # 假如[(0,8), (8,10)], 看8这个时间点是否冲突
        # 不冲突（标准做法）
        #     事件排序方式：points.sort(key=lambda x: (x[0], x[1]))
        #     结束事件 (-1) 优先于开始事件 (1)，确保同一时刻会议室可以被重用。
        # 冲突（需要额外会议室）
        #     事件排序方式：points.sort(key=lambda x: (x[0], -x[1]))
        #     开始事件 (1) 优先于结束事件 (-1)，确保新会议不能重用同一时刻结束的会议室。
        points.sort(key=lambda x: (x[0], x[1]))

        res = 0
        concurrentCount = 0

        for time, val in points:
            # 当扫描到会议开始的时间节点，那么给当前同步进行的会议数量+1
            if val > 0:
                concurrentCount += 1
            # 当扫描到会议结束的时间节点，给当前同步进行的会议数量 -1
            else:
                concurrentCount -= 1

            # 记录在每个扫描线节点的会议数量
            res = max(res, concurrentCount)

        return res

# 古城算法，扫描线: https://docs.google.com/presentation/d/1RGF03Syyw2rhU7MojUWT3G-ejw8NFHEANbgnY2AuDEo/edit#slide=id.g885522199d_0_54
# 这题不能用不相交的区间数量来获取到答案，因为这个边扫边记录最好状态

# lintcode
# https://www.lintcode.com/problem/919/
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        ps = []
        for i in intervals:
            ps.append([i.start, 1])
            ps.append([i.end, -1])
        ps.sort()

        count = 0
        res = 0
        for time, val in ps:
            if val > 0:
                count += 1
            else:
                count -= 1
            res = max(res, count)

        return res