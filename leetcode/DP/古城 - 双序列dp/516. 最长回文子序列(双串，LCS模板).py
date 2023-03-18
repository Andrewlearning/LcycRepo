"""
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

示例 1:
输入:

"bbbab"
输出:
4

一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:

"cbbd"
输出:

2
一个可能的最长回文子序列为 "bb"。
"""
# 使用LCS来做
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = s[::-1]
        return self.lcs(s, r)

    def lcs(self, s, r):
        ls = len(s)
        lr = len(r)

        dp = [[0] * (lr + 1) for _ in range(ls + 1)]

        for i in range(1, ls + 1):
            for j in range(1, lr + 1):
                if s[i - 1] == r[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

"""
古城算法 https://www.youtube.com/watch?v=xUineN8ZqsI&list=PLbaIOC0vpjNW9f04lmGAwVC-856a6y5gw&index=4
24:00

这题的目的，是从s中挑出一个回文子序列，并且这个回文子序列最长
所以我们只要把s反过来(r), 看s和r的最长公共子序列有多长，那么那个就是答案
使用LCS来解决这个题

s = "bbbab"
r = "babbb"

可以看到，正向和reverse的最长共同子序列是"bbbb"
"""



class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = len(s)

        #在子数组 array[i..j] 中，我们要求的子序列（最长回文子序列）的长度为 dp[i][j]
        dp = [[0] * l for i in range(l)]

        # 每个字符自己都是一个回文子串
        for i in range(l):
            dp[i][i] = 1

        # 每次循环我们都以i为中心点向外扩散
        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l, 1):
                # 当i,j相等，那我们就要比较内圈是否相等，如果相等则累加
                # i i+1  j-1 j
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2

                # 当i,j不相等，我们就把当前序列的最大回文串取子串的最大值
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]

"""
https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/zi-xu-lie-wen-ti-tong-yong-si-lu-zui-chang-hui-wen/
"""