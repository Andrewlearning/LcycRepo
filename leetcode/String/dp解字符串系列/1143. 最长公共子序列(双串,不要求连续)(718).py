"""
Example 1:
一个字符串的子序列是指这样一个新的字符串：
它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列, （就是不一定需要是连续的）
但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

找出字符串1和2的最长相同子序列是多长（不要求连续）->例1
"""


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        # 初始化dp数组， dp[text1用了几个字符][text2用了几个字符]时最长公共子序列是多少
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # 我们不用定义初始状态，因为dp[0][0]两个空字符串没有公共序列

        # 从两个字符串的第一个字符开始遍历
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):

                # 假如两个字符相等
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                # 假如两个字符不相等，因为不要求连续
                # 我们只要把距离当前状态最近的两个状态的最值，转移到当前状态就好
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]


"""
本题可以和718放在一起看

https://www.youtube.com/watch?v=Dumq-rceuac
答案：
1. 我们得把这两个字符串，一个放在横轴，一个放在纵轴，dp就是这个矩阵，用来记录当前横纵坐标上的最大递增子序列
2.  _ a b c d e
  _ 0
  a 
  c
  e

我们最好把dp构造得比原数组都长一位，这样方便操作
假如 [i] == [j], 例如 ab ab, 那dp[i][j] = dp[i-1][j-1] + 1 等于 a + 1
假如 [i] != [j], 例如 ab ac, 那么我们就看 max( ab,a  和 a,ac) 看之前这两段，哪段的公共子序列更长，把它更新上去
"""