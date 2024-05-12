"""
给你一个有序的不相交区间列表 intervals 和一个要删除的区间 toBeRemoved
intervals中的每一个区间intervals[i] = [a, b)都表示满足a <= x < b 的所有实数 x的集合。
我们将intervals 中任意区间与toBeRemoved 有交集的部分都删除。
返回删除所有交集区间后，intervals剩余部分的有序列表。

示例 1：
输入：
intervals = [[0,2],[3,4],[5,7]],
toBeRemoved = [1,6]
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
                # 注意这里，头跟头比，尾和尾比
                # interval的左边比remove的左边长，留下[interval[0] ~ remove_head]
                if interval[0] < toBeRemoved[0]:
                    res.append([interval[0], toBeRemoved[0]])

                # interval的右边比remove的右边长，留下[remove_tail ~ intervel[1]]
                if interval[1] > toBeRemoved[1]:
                    res.append([toBeRemoved[1], interval[1]])

                # 假如被删除方完全被 toBeRemoved包裹，那么这个会被完全删除，不计入答案中
                # 最终答案应该是 [start, remove_head] .. [remove_tail, other] .. [others]

        return res

# https://www.youtube.com/watch?v=ihf8JjQdta0 22:06
# 对应lintcode: https://www.lintcode.com/problem/3678/