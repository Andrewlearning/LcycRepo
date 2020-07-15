"""
给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。
在完成所有删除操作后，请你返回列表中剩余区间的数目。

示例：
输入：intervals = [[1,4],[3,6],[2,8]]
输出：2
解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了
"""
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        if not intervals and len(intervals) == 0:
            return 0

        res = 0

        # 按照第一个元素来进行排序的原因是，只有左边先超越了，才有可能实现覆盖别人
        # -x[1]按这个的排序的原因是，有可能出现 [[1,2],[1,4]]这种情况
        # 这时候需要先把[1,4]放前面，然后让2 < 4,也被记录被删除的范围内
        intervals.sort(key=lambda x: (x[0], -x[1]))

        # res记录的是，不用被删除的区间，即使，没有两头被覆盖的区间
        res = 0
        # 上一个区间的末尾所在位置
        cur_end = 0

        for interval in intervals:
            # 因为后一个区间的头，肯定比前一个区间的后
            # 所以假如说 前一个区间[1] >= 后一个区间的[1]，那么就会被覆盖

            # 我们这里取不会被覆盖的情况
            if cur_end < interval[1]:
                res += 1
                cur_end = interval[1]

        return res

# https://leetcode-cn.com/problems/remove-covered-intervals/solution/sao-miao-xian-fa-by-liweiwei1419/