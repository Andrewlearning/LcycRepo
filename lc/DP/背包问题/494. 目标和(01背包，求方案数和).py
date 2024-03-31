"""

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 由于我们计算出的和，有可能为负数，且最极端的状况是-1000
        # 所以我们给所有的j，都加上这个offset，是它始终为正数，最后返回
        offset = 1000

        n = len(nums)

        # dp[i][j] 表示使用nums前i个数字，总和为j的所有方案的集合
        # j的取值范围是[-1000,1000], 由于我们加上了offset, 所以范围变成了[0,2000]
        dp = [[0 for j in range(2001)] for i in range(n + 1)]

        # base case
        # dp[0][0]=1 => 相当于dp[0][1000]=1
        dp[0][offset] = 1

        # 枚举每个物品
        for i in range(1, n + 1):
            # 枚举每个体积
            for j in range(-1000, 1001):
                # 假如 j - nums[i-1] 在体积范围内
                # 我们添加选择这种策略的可能性
                if -1000 <= j - nums[i - 1]:
                    dp[i][offset + j] += dp[i - 1][j - nums[i - 1] + offset]
                # 假如 j + nums[i-1] 在体积范围内
                # 我们添加选择这种策略的可能性
                if j + nums[i - 1] <= 1000:
                    dp[i][offset + j] += dp[i - 1][j + nums[i - 1] + offset]

        return dp[n][offset + target]


"""
# 这个做法是没有压缩的
https://www.acwing.com/video/1899/
dp[i][j] 表示使用nums前i个数字，能生成多少个总和为j的组合

递推式
dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]]
当前i个数组成总和为j的组合
是   前i-1个数，所组成总和为(j - nums[i])的数量
和   前i-1个数，所组成总和为(j + nums[i])的数量
之和构成的
"""
