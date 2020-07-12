"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
"""
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
        return dp[n]

# 链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/xiang-jie-bao-li-di-gui-ji-yi-hua-ji-zhu-dong-tai-/