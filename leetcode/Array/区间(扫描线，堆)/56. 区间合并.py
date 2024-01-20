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
        if not itvs or len(itvs) == 0:
            return []

        itvs.sort(key = lambda x: x[0])
        # itvs.sort()也行，默认是按第一个元素排序的

        res = []
        # 先记录第一个区间的左右断点
        p = itvs[0]

        for i in range(1, len(itvs)):
            cur = itvs[i]
            #  情况2.2，两个区间没有交集
            if p[1] < cur[0]:
                # 记录当前区间
                res.append(p)
                # 切换到下一个区间
                p = cur
            # 情况2.1，两个区间有交集
            else:
                # 更新当前区间的右端点
                p[1] = max(p[1], cur[1])

        # 保存最后一个区间
        res.append(p)
        return res

"""
https://www.acwing.com/video/1393/
Time complexity : O(nlogn)
Space complexity : O(1) (or O(n))
答案：
此题思路不难
1. 按照左端点排序
2.1 如果上一个区间和下一个区间有交集，则更新上一个区间的右端点
2.2 如果上一个区间和下一个区间无交集，则保存当前区间，并把l,r却换到下一个区间继续查找
"""