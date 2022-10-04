class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dp[i][j]
        # 在i遍历的硬币范围内，我们要在[0,i]范围内选硬币，才能使得硬币和为j的方案数，最大有多少
        dp = [0] * (amount + 1)

        # 当值为0的时候，我们有唯一方案就是不选任何硬币
        # 这相当于dp[0~i][j] = 0
        dp[0] = 1

        # 枚举每个物品
        for i in range(len(coins)):
            # 枚举每个合法体积[coins[i], amount]
            for j in range(coins[i], amount + 1):
                # dp[j]的方案数 = 选用当前[0, i]硬币方案数之和
                dp[j] += dp[j - coins[i]]

        return dp[-1]


"""
https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-ii-by-leetcode/
这个解析讲的很好， 这题本质上有点像跳台阶， 

当前这一遍dp[i] 的值，等于上一遍dp[i]的值 + 加上这枚硬币到这一步的可能性
"""