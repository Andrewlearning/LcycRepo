"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False

        # dp[i] 表示，当有i个字符时，是否可以拼成一个单词
        dp = [False for _ in range(len(s) + 1)]

        # 初始化
        dp[0] = True

        # i,j代表的是s的下标，对应到dp上是i+1, j+1
        # 假如说i = True, 那就是dp[i+1] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                # dp[i] 表示s[0, i-1]可以拼成单词
                # s[i: j+1] 表示s[i, j] 可以拼成单词
                if dp[i] and s[i: j + 1] in wordDict:
                    dp[j + 1] = True

        return dp[-1]

"""
// Time: O(n^2), Space: O(n+m)
https://algocasts.io/episodes/Z5mzgJGd
https://leetcode.com/problems/word-break/discuss/43995/A-Simple-Python-DP-solution
答案：
1.这题dp的做法有点特别
2.dp[i]表示，从上一个true的未知，到i的位置，这个串，是否在字典里面
3.dp[i] = True，同时表示着，以当前i为字母的开头，能否找到[i，j],存在于字符串里面
例子    l e e t c o d e    {"leet","code"}
dp      t f f f t f f f t  (dp[i] = True每一个都刚好压在字典里每个单词的开始，导致每个单词
                            都可以被找到，return dp[-1]时为True）

反例     l e e t c o d e    {"leetc","code"}
         t f f f f t f f f (因为第一个单词把结尾T放在了O上，导致了第二个code根本无法找到
                            所以dp[-1] = False)

"""