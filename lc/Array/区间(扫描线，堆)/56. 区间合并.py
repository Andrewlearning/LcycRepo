"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6]
"""
class Solution(object):
    def merge(self, itvs):
        """
        :type itvs: List[List[int]]
        :rtype: List[List[int]]
        """
        # 按照区间第一个元素进行排序
        itvs = sorted(intervals)
        n = len(itvs)
        res = []

        i = 0
        while i < n:
            cur = itvs[i]

            # 看当前区间和下一个区间可不可以融合
            while i + 1 < n and cur[1] >= itvs[i + 1][0]:
                cur[1] = max(cur[1], itvs[i + 1][1])
                i += 1

            # 每次把融合结束，或者没办法融合的区间给加进res
            res.append(cur)
            i += 1
        return res

"""
https://www.acwing.com/video/1393/
Time complexity : O(nlogn)
Space complexity : O(1) (or O(n))
答案：
此题思路不难
1. 按照左端点排序
2.1 如果上一个区间和下一个区间有交集，则更新上一个区间的右端点
2.2 如果上一个区间和下一个区间无交集，则保存当前区间
"""