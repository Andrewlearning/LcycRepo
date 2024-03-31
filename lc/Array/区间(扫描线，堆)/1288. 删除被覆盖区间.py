"""
给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
只有当c <= a且b <= d时，我们才认为区间[a,b) 被区间[c,d) 覆盖。
在完成所有删除操作后，请你返回列表中剩余区间的数目。

示例：
输入：nums = [[1,4],[3,6],[2,8]]
输出：2
解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了
"""
class Solution(object):
    def removeCoveredIntervals(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        if not nums and len(nums) == 0:
            return 0

        # 头按从小到大排，尾从大到小排, 因为这样方便我们后面筛选
        # 例如这个case [[1,2],[1,4],[3,4]]
        # 我们想让它按照 [[1,4],[1,2],[3,4]]
        nums.sort(key=lambda x: (x[0], -x[1]))

        # 被删除的区间
        removeCount = 0

        # 上一个区间覆盖他人区间的末尾所在位置，我们用这个判断能不能覆盖下一个区间
        maxRight = nums[0][1]

        n = len(nums)

        for i in range(1, n):
            # 因为上一个没被覆盖区间的头总是 <= 下一个区间的区间头
            # 所以我们只用判断 下一个区间的区间尾 <= 上一个没被覆盖区间的区间尾 就知道能不能进行覆盖了
            # 假如 下一个区间的区间尾 <= 上一个没被覆盖区间的区间尾，说明可以覆盖
            if nums[i][1] <= maxRight:
                removeCount += 1
            # 假如 下一个区间的区间尾 > 上一个没被覆盖区间的区间尾, 说明无法覆盖，更新maxright
            else:
                maxRight = nums[i][1]

        return len(nums) - removeCount

# https://leetcode-cn.com/problems/remove-covered-nums/solution/sao-miao-xian-fa-by-liweiwei1419/