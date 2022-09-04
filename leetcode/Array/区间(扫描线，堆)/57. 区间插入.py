"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
注意：这题题目给的intervals是排序好的
"""
class Solution(object):
    def insert(self, old, new):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        k = 0
        # 左边无交集部分，老区间的右端点 < 新区间的左端点
        while k < len(old) and old[k][1] < new[0]:
            res.append(old[k])
            k += 1

        # 中间有交集部分
        if k < len(old):
            # 先更新交集区间的左端点，这个只需要更新一次
            new[0] = min(old[k][0], new[0])

            # 持续更新区间的右端点
            while k < len(old) and old[k][0] <= new[1]:
                new[1] = max(old[k][1], new[1])
                k += 1

        # 然后把合并好的区间加到答案里
        res.append(new)

        while k < len(old):
            res.append(old[k])
            k += 1

        return res


"""
Time:O(n) space: O(n)
三种情况
1. 左边无交集部分
2. 中间有交集部分
3. 右边无交集部分
"""

