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

        n = len(s)
        # dp[i] 表示，在s[0, i-1]这段字符串里，可以分割成一个或多个单词存在与wordDict里，
        dp = [False] * (n + 1)

        # 初始化，一个字母都没有的时候 = True
        # 因为这个后续可以帮助第一个单词的拆解
        dp[0] = True

        # 优化一下单词的查询时间
        wordMap = {}
        for word in wordDict:
            wordMap[word] = True

        # i,j代表的是s的下标，对应到dp上是i+1, j+1
        # 我们通过判断 s[0,i-1] 和 s[i,j] 这两段，是否都可以拆分成在wordDict中的单词
        for i in range(n):
            if dp[i] == True:
                for j in range(i, n):
                    # dp[i] 表示s[0, i-1]可以拼成单词
                    # s[i,j+1] 表示s[i, j] 可以拼成单词
                    if s[i: j+1] in wordMap:
                        dp[j+1] = True

        return dp[n]

"""
// Time: O(n^2), Space: O(n+m)
可以前面听听思路，做法不完全一样
https://www.acwing.com/video/1505/
"""