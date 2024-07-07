"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute ！！！the fewest number of coins！！！ that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
找出最少需要多少硬币才能拼成amount
"""
# 记忆化搜索
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @cache
        def dfs(i, c):
            if i < 0:
                # 当c=0的时候，说明我们找到一个合法方案，返回0，因为在递归的时候已经在+1了
                # 当c!=0的时候，说明方案不合法，返回inf, 让后面min处理的时候抛弃这个方案
                return 0 if c == 0 else float('inf')
            if c < coins[i]:
                return dfs(i - 1, c)
            # 这里的背包值我们看做是1，表示使用了多少枚硬币
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)

        res = dfs(n - 1, amount)
        # 有可能所有的方案都是不合法的
        if res == float('inf'):
            return -1
        return res

"""
https://www.bilibili.com/video/BV16Y411v7Y6/?spm_id_from=333.337.search-card.all.click&vd_source=b81616a45fd239becaebfee25e0dbd35
完全背包:
有n种物品，第i种物品的体积为w[i]，价值为v[i]每种物品无限次重复选，求体积和不超过capacity时的最大价值和

当前操作?
枚举第之种物品选一个或不选:
不选，剩余容量不变
选一个，剩余容量减少w[i]

分类讨论
不选, 在剩余容量为c时, 从前i-1种物品中得到的最大价值和
选1个, 在剩余容量为c-w[i]时, 从前i种物品中得到的最大价值和
dfs(i,c)= max(dfs(i-1,c), dfs(i,c-w[i]) + v[i])


完全背包变形 - 求最小方案数

至多装 capacity，求方案数/最大价值和
恰好装 capacity，求方案数/最大/最小价值和
至少装 capacity，求方案数/最小价值和
dfs(i,c) = min(dfs(i-1,c), dfs(i,c-w[i]) + v[i])
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i][j]
        # i表示，选用coins [0~i]范围以内的硬币
        # j表示，在coins[0~i]范围内，我们要在其中最少选用多少次硬币，才能使得硬币和为j，且使用硬币数量最少
        dp = [float('inf')] * (amount + 1)

        # base case, 构成和为0，需要任何0枚硬币
        dp[0] = 0

        # 遍历每个石头
        for i in range(len(coins)):
            # 遍历每个体积，从小到大，遍历范围[coins[i], amount]
            for j in range(coins[i], amount + 1):

                # 假如我们不使用coins[i], 那么dp[j] = dp[j], 所以我们可以省略
                # 假如我们使用coins[i], 那么dp[j] = dp[j - nums[i]] + 1
                # min表示上面两种方案取最小值
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        # 假如硬币无法凑成目标amount, dp[amount]应该的值应该是没更改过的
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]


"""
答案： time O^2
https://www.acwing.com/video/1709/
如果还有问题看AcWing 3
"""