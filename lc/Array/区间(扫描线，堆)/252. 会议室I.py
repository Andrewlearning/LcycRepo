# -*- coding: utf-8 -*-
"""
给出开会时间，问一个人能不能同时参加所有会议（就是会议之间不能有交集）
Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
"""

# 这种做法可以，但是比较naive, 本质上我们希望找到不重叠区间的个数，利用452的做法笔记哦啊好
class Solution(object):
    def meetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: Boolean
        """
        intervals.sort(key=lambda x: x[0])
        for i in range(1,len(intervals)):
            # 后一个区间和前一个区间有交集，则一个人不可能参加所有回忆
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    testList = [
        [[0, 30], [5, 10], [15, 20]],
        [[7, 10], [2, 4]]
    ]
    resList = [
        False,
        True
    ]
    for i in range(len(testList)):
        res = s.meetingRooms(testList[i])
        if res == resList[i]:
            print("test case " + str(i) + " success")
        else:
            print("test case " + str(i) + " false")

"""
可以到lintcode写: https://www.lintcode.com/problem/920/description
Time:O(nlogn), Space:O(1)
答案：
1.排序
2.检查是否有 后.start < 前.end
  有的话则说明这个人去不了，因为前一个开会时间太长了，他赶不上不后面的
"""

# lintcode答案1
class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            # 后一个区间和前一个区间有交集，则一个人不可能参加所有回忆
            if intervals[i-1].end > intervals[i].start:
                return False
        return True

# lintcode答案2，利用452题的做法，尾部排序，求出不相交区间的数量
class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True

        intervals.sort(key=lambda x: x.end)
        cur = intervals[0].end

        # 假如不重叠区间的数量等于会议数量，则说明一个人可以参加所有会议
        res = 1

        for i in range(1, len(intervals)):
            # 对于会议室这个题，两个时间重合了，也可以看做是不相交区间
            if cur <= intervals[i].start:
                res += 1
                cur = intervals[i].end

        if res == len(intervals):
            return True
        return False