"""
给你一个区间数组 intervals ，其中intervals[i] = [starti, endi] ，且每个starti 都不同 。

区间 i 的 右侧区间定义: 存在区间j ，并满足 startj >= endi ，且 startj 最小化 。

返回一个由每个区间 i 的 右侧区间 在intervals 中对应下标组成的数组。
如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。

输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。
"""

class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)

        # 排序前给每一个区间的末尾添加索引，因为我们最终答案要返回索引
        for i in range(n):
            intervals[i].append(i)

        # 按区间按左端点的进行排序
        intervals.sort(key=lambda x: x[0])

        # 储存每个区间的最接近的右区间的下标
        res = [-1] * n

        for cur in intervals:
            targetRight = cur[1]
            tragetIndex = cur[2]

            l = 0
            r = n - 1
            # 因为我们想要找到离当前intervel最近的合法右区间，34题模板
            # 所以我们用往左边界查找的方法来进行查找
            # 这样能找到: 存在区间j ，并满足 startj >= endi ，且startj最小
            while l < r:
                mid = (l + r) // 2
                if targetRight <= intervals[mid][0]:
                    r = mid
                else:
                    l = mid + 1

            # 假如存在，那么更新这个intervel的最近右区间的下标
            if intervals[r][0] >= targetRight:
                res[tragetIndex] = intervals[r][2]

        return res


# 思路： https://www.acwing.com/video/1838/
