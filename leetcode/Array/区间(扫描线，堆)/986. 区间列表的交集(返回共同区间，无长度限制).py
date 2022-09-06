"""
给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。

返回这两个区间列表的交集。

输入：A = [[0,2],[5,10],[13,23],[24,25]],
    b = [[1,5],[8,12],[15,24],[25,26]]

输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]
"""
class Solution(object):
    def intervalIntersection(self, a, b):
        """
        :type A: List[List[int]]
        :type b: List[List[int]]
        :rtype: List[List[int]]
        """

        pa = 0
        pb = 0
        na = len(a)
        nb = len(b)
        res = []

        while pa < na and pb < nb:
            # 限定有交集时间的最小值
            # 假如说出现两个区间不想交的情况，maxStart 比 minEnd
            maxStart = max(a[pa][0], b[pb][0])
            minEnd = min(a[pa][1], b[pb][1])

            # 只要有共同时间，那么我们就把他加进res
            if minEnd - maxStart >= 0:
                res.append([maxStart, minEnd])

            # 不管有没有共同时间，我们都移动到下一位
            # 移动原则是，看谁早结束，就移动哪个
            if a[pa][1] < b[pb][1]:
                pa += 1
            else:
                pb += 1

        return res

# https://leetcode.cn/problems/interval-list-intersections/solution/qu-jian-lie-biao-de-jiao-ji-by-leetcode/