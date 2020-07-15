"""
是一名行政助理，手里有两位客户的空闲时间表：slots1 和 slots2，以及会议的预计持续时间 duration，请你为他们安排合适的会议时间。
「会议时间」是两位客户都有空参加，并且持续时间能够满足预计时间 duration 的 最早的时间间隔。
如果没有满足要求的会议时间，就请返回一个 空数组。
「空闲时间」的格式是 [start, end]，由开始时间 start 和结束时间 end 组成，表示从 start 开始，到 end 结束。 
题目保证数据有效：同一个人的空闲时间不会出现交叠的情况，也就是说，对于同一个人的两个空闲时间 [start1, end1] 和 [start2, end2]，要么 start1 > end2，要么 start2 > end1。


示例 1：
输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
输出：[60,68]
"""


class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        # 把两个数组根据开始时间来排序
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        p1 = 0
        p2 = 0
        n1 = len(slots1)
        n2 = len(slots2)

        while p1 < n1 and p2 < n2:

            # 限定有交集时间的最小值
            intersectStart = max(slots1[p1][0], slots2[p2][0])
            intersectEnd = min(slots1[p1][1], slots2[p2][1])

            # 假如说共同时间大于 要求的时间，那么我们返回结果
            if intersectEnd - intersectStart >= duration:
                return [intersectStart, intersectStart + duration]

            # 假如说共同时间小于 要求的时间，那么我们把比较小的时间换到下一位
            elif slots1[p1][1] < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1