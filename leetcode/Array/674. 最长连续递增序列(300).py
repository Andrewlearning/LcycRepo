"""
给定一个未经排序的整数数组，找到最长且连续的的递增序列。
中点是连续
"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums and len(nums) == 0:
            return 0

        dp = [1 for _ in range(len(nums))]
        res = 0

        for i in range(len(nums)):
            # 只有满足nums[i - 1] < nums[i]的时候，我们才能算作连续递增
            if i > 0 and nums[i - 1] < nums[i]:
                dp[i] = max(dp[i], dp[i - 1] + 1)

            # 记录
            res = max(res, dp[i])

        return res

"""
就是对比前后两个数字，如果递增，temp += 1
如果不递增，那么temp = 1
"""