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

        # base case, 构成和为0，需要0枚硬币
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