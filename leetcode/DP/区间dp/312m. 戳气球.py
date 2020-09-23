"""
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = [1] + nums + [1]
        # dp[i,j]表示集合中[i+1,j-1]气球打完的最大值方案
        dp = [[0] * len(nums) for i in range(len(nums))]

        # 因为我们一个区间，有三个指针，所以初始长度最少为3
        # 我们这个区间的最大范围是len(num)
        for midRange in range(3, len(nums) + 1):
            # i是中间区间的左边界
            i = 0
            while i + midRange - 1 < len(nums):
                # j最多到len(nums) - 1
                j = i + midRange - 1

                # k的移动范围[i+1, j-1]
                # 这个区间内i*k*j的最大值 max(nums[i]*nums[k]*nums[j])
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])
                i += 1

        return dp[0][-1]

"""
时间 n**3
https://www.acwing.com/video/1702/
"""