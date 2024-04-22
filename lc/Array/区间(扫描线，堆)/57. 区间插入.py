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
        n = len(old)

        # 用k来作为遍历的old的下标
        k = 0
        # 左边无交集部分，老区间的右端点 < 新区间的左端点
        while k < n and old[k][1] < new[0]:
            res.append(old[k])
            k += 1
        # 假如遍历完old还没有遇到交集，则说明new可以直接加在最后面
        if k == n:
            res.append(new)
            return res

        # 中间有交集部分
        # 持续更新区间的右端点
        # 我们怎么确认还有交集，new[1] >= old[k][0]，就说明还有交集
        while k < n and new[1] >= old[k][0]:
            new[0] = min(new[0], old[k][0])
            new[1] = max(new[1], old[k][1])
            i += 1
        # 然后把合并好的区间加到答案里
        res.append(new)

        # 把剩余没有交集的区间也加入到res中
        while k < n:
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

