class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 记录当长度为i时，的最大乘积
        dp = [0 for _ in range(n + 1)]  # dp[0] dp[1]其实没用

        # 1 * 1 = 1
        dp[2] = 1
        res = -1

        for i in range(3, n + 1):
            for j in range(i):
                # (i-j) * j 等于是只剪一次
                # j * dp[i - j] 等于是，剪一段长度为j的下来，剩下的用之前的最优解去乘
                dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
        return dp[n] % 1000000007

# 链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/xiang-jie-bao-li-di-gui-ji-yi-hua-ji-zhu-dong-tai-/