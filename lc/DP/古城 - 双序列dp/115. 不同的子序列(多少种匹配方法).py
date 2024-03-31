"""
给定一个字符串S和一个字符串T，计算在 S 的子序列中 T 出现的个数。
一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE"是"ABCDE"的一个子序列，而"AEC"不是）
题目数据保证答案符合 32 位带符号整数范围。

示例1：

输入：S = "rabbbit", T = "rabbit"
输出：3
解释：

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
"""
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ns = len(s)
        nt = len(t)

        # dp[s][t], s[0,i]所有和t[0,j]相等的子序列数量
        dp = [[0] * (nt + 1) for _ in range(ns + 1)]

        # 初始化
        for i in range(ns + 1):
            dp[i][0] = 1

        for i in range(1, ns + 1):
            for j in range(1, nt + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]

"""
链接：https://www.acwing.com/video/1470/

对于s[i], 我们有两种选择

1. 我们不使用s[i]
那么dp[i][j] 的相等子序列数量 = dp[i-1][j]

2. 我们使用s[i]
当我们选择使用s[i]的时候，我们有前提条件s[i] = t[j]，要不然选择使用s[i]是没有意义的
所以dp[i][j] 的相等子序列数量 = dp[i-1][j-1]

所以对于dp[i][j] = 上面两种情况的和
"""
