"""
每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

lefti 是第 i 座建筑物左边缘的 x 坐标。
righti 是第 i 座建筑物右边缘的 x 坐标。
heighti 是第 i 座建筑物的高度。
你可以假设所有的建筑都是完美的长方形，在高度为 0的绝对平坦的表面上。

天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。
关键点是水平线段的左端点。

"""

from sortedcontainers import SortedList
class Solution(object):
    def getSkyline(self, buildings):
        res = []
        points = []
        # 我们想让最高的左端点被优先遍历到，因为这样便于我们记录答案
        # 对于设置正负，我们是为了区分出左端点和右端点，以及在边界情况下怎么区分
        for l, r, h in buildings:
            points.append((l, -h))
            points.append((r, h))

        # 按照点的x坐标进行 小->大 排序
        # 左端点高度 高 -> 矮排序，按照相同x坐标 左端点 -> 右端点排序
        # 右端点高度 矮 -> 高排序
        points.sort()

        # 当前扫描线所停留位置的所有建筑最大高度，设定一个默认高度为0, 0用于当垂线只有建筑右端点的情况
        # SortedList默认是从小到大排序
        # 后面用的时候，排序为 [左端点高度, 0, 右端点高度]
        lineHeights = SortedList([0])

        # 上一个建筑最高高度
        prev = 0
        for x, h in points:
            if h < 0:
                # h<0, 说明遍历到左节点了，记录当前建筑的高度
                lineHeights.add(h)
            else:
                # h>0, 说明遍历到右节点了，删除当前建筑的高度
                lineHeights.remove(-h)

            # 加入或删除后，在当前扫描线垂线中所有建筑物的最高高度
            curr_max = abs(lineHeights[0])

            # 最高高度发生了变化
            # 1. 出现了新的，高度不一样的左端点
            # 2. 遍历到右端点，在同一垂线下，有不一样高度的建筑，记录不一样高度的建筑
            # 3. 遍历到右端点，在同一垂线下，无不一样高度的建筑，记录0
            if curr_max != prev:
                res.append([x, curr_max])

            # 这个非常重要，记录了上一个水平线的高度
            prev = curr_max
        return res
"""
n 是矩形数量
Time: O(nlogn), Space: O(n)

思路有参考acwing
https://www.acwing.com/activity/content/problem/content/2599/

acwing文字讲解，我们如何对高度进行排序处理，三种情况
https://www.acwing.com/solution/content/4607/

代码来源
https://leetcode.cn/problems/the-skyline-problem/solution/python-yi-ci-bian-li-suo-you-fa-sheng-ji-1sht/
"""