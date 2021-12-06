class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)

        # 总和不能刚好被平分成两份，所以不可能构成
        if total % 2 == 1:
            return False

        # 每一份数应该是1/2个total
        total //= 2

        dp = [[False for j in range(total + 1)] for i in range(len(nums))]

        # base case, 使用前i个数，合为0，那么就是所有的数都不去选择
        for i in range(len(nums)):
            dp[i][0] = True

        for i in range(1, len(nums)):
            for j in range(1, total + 1):

                # 说明当前num刚好能填满背包
                if nums[i] == j:
                    dp[i][j] = True
                    continue

                # 当前num不能仅靠自己填满背包，那我们要看看
                # [0- i-1]个数可不可以填满背包
                # 加上当前这个数，能不能填满背包
                if nums[i] < j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                # 假如nums[i] 大于背包容量，那么就不应该考虑把这个数加进背包
                if nums[i] > j:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][total]


"""
时间复杂度：O(NC)：这里 N是数组元素的个数, C 是数组元素的和的一半。
空间复杂度：O(NC)
https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/

如何理解本题的状态转移方程：
dp[i][j]表示从数组的 [0, i] 这个子区间内挑选一些正整数，每个数只能用一次，使得这些数的和恰好等于 j
dp[i][j]表示，对于前 i 个物品，当前背包的容量为j时
    若 dp[i][j] 为 true，则说明有一种选择方法的和为j
    若 dp[i][j] 为 false，则说明没有有一种选择方法的和为j
比如说，如果 dp[4][9] = true，其含义为：对于容量为 9 的背包，若只是用前 4 个物品，至少有一种可能能刚好装到9。

状态转移方程：
1、不选择 nums[i]，如果在 [0, i - 1] 这个子区间内已经有一种选择方法的使得它们的和为 j ，那么 dp[i][j] = true；
2、选择 nums[i]，如果在 [0, i - 1] 这个子区间内就得找到一部分元素，使得它们的和为 j - nums[i]。
"""