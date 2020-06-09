"""
给定 m 个数组，每个数组都已经按照升序排好序了。现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数 a 和 b 之间的距离定义为它们差的绝对值 |a-b| 。你的任务就是去找到最大距离

示例 1：

输入：
[[1,2,3],
 [4,5],
 [1,2,3]]
输出： 4
解释：
一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。
（不能选择同一个数组的最大最小值得到答案）
"""

import sys


class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        max_value = -sys.maxsize
        min_value = sys.maxsize
        res = 0

        for i in range(len(arrays)):
            # tempmin, max表示当前回合的最大最小值
            tmpMin = arrays[i][0]
            tmpMax = arrays[i][-1]

            # 题目规定我们不能用同一个数组的最大最小值相减得到答案
            # 所以我们要用这次的减去上次的
            res = max(max_value - tmpMin, tmpMax - min_value, res)

            # 更新
            max_value = max(max_value, tmpMax)
            min_value = min(min_value, tmpMin)

        return res
