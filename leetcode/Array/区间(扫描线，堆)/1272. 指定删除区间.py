"""
给你一个 有序的 不相交区间列表 intervals 和一个要删除的区间 toBeRemoved， intervals 中的每一个区间 intervals[i] = [a, b] 都表示满足 a <= x < b 的所有实数  x 的集合。
我们将 intervals 中任意区间与 toBeRemoved 有交集的部分都删除。
返回删除所有交集区间后， intervals 剩余部分的 有序 列表。

示例 1：
输入：intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
输出：[[0,1],[6,7]]
"""
class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        if not intervals and len(intervals) == 0:
            return []

        res = []
        for interval in intervals:
            # 两个区间没有重叠部分, 那么意味着不用进行删除
            if interval[1] <= toBeRemoved[0] or toBeRemoved[1] <= interval[0]:
                res.append(interval)
            # 两个区间有重叠部分
            else:
                # interval的左边比remove的左边长，[interval  )[remove]
                if interval[0] < toBeRemoved[0]:
                    res.append([interval[0], toBeRemoved[0]])

                # interval的右边比remove的右边长， [remove]( interval]
                if interval[1] > toBeRemoved[1]:
                    res.append([toBeRemoved[1], interval[1]])

        return res

