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

class Solution(object):
    def meetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: Boolean
        """
        intervals.sort(key=lambda x: x[0])
        for i in range(1,len(intervals)):
            # 后一个区间和前一个区间有交集，则一个人不可能参加所有回忆
            if intervals[i-1][1] >= intervals[i][0]:
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
Time:O(nlogn), Space:O(1)
答案：
1.排序
2.检查是否有 后.start < 前.end
  有的话则说明这个人去不了，因为前一个开会时间太长了，他赶不上不后面的
"""
