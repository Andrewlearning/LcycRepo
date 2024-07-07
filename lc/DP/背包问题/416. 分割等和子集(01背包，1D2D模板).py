"""
给你一个 只包含正整数 的 非空 数组 nums。
请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11]
"""

# 记忆化搜索，超空间
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def dfs(i, c):
            if i < 0:
                # 假如刚好到我们的目标，c=0, 则说明这是一个有效方案，返回1，否则返回0
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i - 1, c)
            # 记录选 + 不选，这两种方案数之和
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])

        s = sum(nums)
        if s % 2 == 1:
            return False
        return dfs(n - 1, s // 2)

"""
0-1背包: 有n个物品，第i个物品的体积为w[i]，价值为v[i], 每个物品至多选一个，求体积和不超过capacity时的最大价值和

当前操作?枚举第i个物品选或不选:
不选，剩余容量不变;
选，剩余容量减少

分类讨论选不选:
在剩余容量为c时, 从前i-1个物品中得到的最大价值和
在剩余容量为c-w[i]时，从前i-1个物品中得到的最大价值和
dfs(i,c) = max(dfs(i-1,c), dfs(i-1,c-w[i])+ v[i])

    def dfs(i, c):
        if i < 0:
            return 0
        if c < nums[i]:
            return dfs(i - 1, c)
        return max(dfs(i - 1, c), dfs(i - 1, c - nums[i]) + w[i])


本题是0-1背包的变形 - 求方案数
01背包常见变形
至多装 capacity，求方案数/最大价值和
恰好装 capacity，求方案数/最大/最小价值和
至少装 capacity，求方案数/最小价值和

从前i-1个数中，不选择当前数，选一些数恰好组成c的方案数，dfs(i-1,c)
从前i-1个数中，选择当前数，选一些数恰好组成c - w[i]的方案数，dfs(i-1,c - w[i])
所以dfs(i,c)的总方案数: dfs(i,c) = dfs(i-1,c) + dfs(i-1,c - w[i])

https://www.bilibili.com/video/BV16Y411v7Y6/?spm_id_from=333.337.search-card.all.click&vd_source=b81616a45fd239becaebfee25e0dbd35
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)
        n = len(nums)

        # 总和不能刚好被平分成两份，所以不可能构成
        if total % 2 == 1:
            return False

        # 每一份数的和 应该是1/2 total
        targer = total // 2

        # dp[i][j]
        # 从前i个数中选择，他们的目标和是否能达到j
        # i=0表示什么数都不选，i=2表示(不选，选第一个数，选第二个数)
        dp = [[False] * (targer + 1) for i in range(n+1)]

        # base case, 使用前i个数，目标和为0，只要所有的数都不去选择，那么就能满足和为0
        # 所以都为True
        for i in range(n):
            dp[i][0] = True

        # 枚举每个物品
        # i从1开始是因为要跟[i-1]作对比
        for i in range(1, n + 1):
            # 枚举体积，从小到大
            for j in range(1, targer + 1):
                # 如果当前数大于目标和，无法选择该数
                dp[i][j] = dp[i-1][j]

                # 可以选择或不选择当前数
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]

        return dp[n][targer]


"""
时间复杂度：O(N*C)：这里 N是数组元素的个数, C 是数组元素的和的一半。
空间复杂度：O(N*C)
古城算法: https://www.youtube.com/watch?v=OJ3ykzYCsLQ 12:00
acwing较为详细的推导: https://www.acwing.com/video/944/
"""

# 压缩到一维，因为因为我们只会用到 dp[i] 和 dp[i-1]的状态
# 所以我们可以把i这一个纬度给去掉
class Solution(object):
    def canPartition1D(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)

        # 总和不能刚好被平分成两份，所以不可能构成
        if total % 2 == 1:
            return False

        # 每一份数应该是1/2个total
        targer = total // 2

        # dp[i] 从已被遍历到的数的范围内进行选择，看被选择的数的和 是否能等于 i
        dp = [False] * (targer + 1)

        # base case, 从所有数来选择，目标和为0，只要所有的数都不去选择，那么就能满足和为0
        # 所以都为1
        dp[0] = True

        # 枚举每个物品
        for i in range(len(nums)):
            # 从大到小枚举体积, 枚举范围[nums[i], targer]
            for j in range(targer, nums[i] - 1, -1):

                # 假如我们不使用nums[i], 那么dp[j] = dp[j], 所以我们可以省略
                # 假如我们使用nums[i], 那么dp[j] = dp[j - nums[i]]
                # |(or) 是表明我们从上面两种选法中取其中的最优解来记录
                dp[j] = dp[j - nums[i]] | dp[j]

        return dp[-1]

