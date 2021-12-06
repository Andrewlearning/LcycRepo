"""

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        offset = 1000
        n = len(nums)
        dp = [[0 for j in range(2001)] for i in range(n + 1)]

        # dp[i][j] 表示使用nums前i个数字，能生成多少个总和为j的组合
        # 考虑到 -1000 <= target <= 1000， 因为数组下标不能用负数来表示，所以我们把下标 0 -> 1000
        # 所以原来 -1000 ~ 0 ~ 1000 => 0 ~ 1000 ~ 2000
        # 所以dp[0][0] => dp[0][1000]
        dp[0][offset] = 1

        for i in range(1, n + 1):
            for j in range(-1000, 1001):
                # 因为目标数 j - nums[i-1] 有可能会是负数。所以我们要保证目标数是在这个范围以内的
                if -1000 <= j - nums[i - 1] <= 1000:
                    dp[i][offset + j] += dp[i - 1][offset + j - nums[i - 1]]
                # 同样的，确定目标数不要越界
                if -1000 <= j + nums[i - 1] <= 1000:
                    dp[i][offset + j] += dp[i - 1][offset + j + nums[i - 1]]

        return dp[n][offset + S]


"""
https://www.acwing.com/video/1899/
dp[i][j] 表示使用nums前i个数字，能生成多少个总和为j的组合

递推式
dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]]
当前i个数组成总和为j的组合
是有 前i-1个数，所组成总和为(j - nums[i])的数量
和   前i-1个数，所组成总和为(j + nums[i])的数量
之和构成的
"""
