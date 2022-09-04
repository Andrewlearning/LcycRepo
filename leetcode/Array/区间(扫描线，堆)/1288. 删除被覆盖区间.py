"""
给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
只有当c <= a且b <= d时，我们才认为区间[a,b) 被区间[c,d) 覆盖。
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

        # 头按从小到大排， 尾从大到小排
        intervals.sort(key=lambda x: (x[0], -x[1]))

        # res记录的是，不用被删除的区间，即是，没有两头被覆盖的区间
        res = 0

        # 上一个区间的末尾所在位置
        last_end = 0

        for cur in intervals:
            # 因为 last_head <= cur_head
            # 所以我们要保证不出现  last_head <= cur_head < cur_end <= last_end就好饿了

            # 我们这里取不会被覆盖的情况
            if last_end < cur[1]:
                res += 1
                last_end = cur[1]

        return res

# https://leetcode-cn.com/problems/remove-covered-intervals/solution/sao-miao-xian-fa-by-liweiwei1419/

# https://leetcode-cn.com/problems/remove-covered-intervals/solution/sao-miao-xian-fa-by-liweiwei1419/