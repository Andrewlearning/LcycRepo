"""
Given a string s. In one step you can insert any character at any index of the string.
Return the minimum number of steps to make s palindrome.
A Palindrome Stringis one that reads the same backward as well as forward.

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

"mbadm" -> "mbdadbm" 需要概念两个字符才能形成回文
"""

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = s[::-1]
        common = self.lcs(s, r)
        return len(s) - common

    # 套用1143的模板
    # 假如一个字符串回文，那么正向的s和翻转后的r 应该所有字符都一样
    # 假如一个字符串不回文，那么正向的s和翻转后的r, 若存在不相等的字符，那么久意味着那些字符我们需要添加，已构成回文
    # 这个method能求出两个字符串的共同元素有多少
    # 所以用len(s) - lcs 就能求出两个字符串不相等的元素个数有多少 -> 即是我们需要添加的元素
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

# https://www.youtube.com/watch?v=xUineN8ZqsI&list=PLbaIOC0vpjNW9f04lmGAwVC-856a6y5gw&index=4
