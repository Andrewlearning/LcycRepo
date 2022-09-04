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

        list = []
        for interval in intervals:
            # 1 会议开始，1表示记录这个房间
            # -1 会议结束，-1取消对这个房间的追踪
            list.append((interval[0], 1))
            list.append((interval[1], -1))

        # 我们首先按照房间的开始时间来排序从先到后排序
        # 其次再由房间的结束时间从先到后进行排序，这样处理掉先结束的会议又可以空出新的房间
        # 可以直接list.sort()
        list.sort(key=lambda x: (x[0], x[1]))

        res = 0
        concurrentCount = 0

        for time, val in list:
            # 当扫描到会议开始的时间节点，那么给当前同步进行的会议数量+1
            if val > 0:
                concurrentCount += 1
            # 当扫描到会议结束的时间节点，给当前同步进行的会议数量 -1
            else:
                concurrentCount -= 1

            # 记录在每个扫描线节点的会议数量
            res = max(res, concurrentCount)

        return res

