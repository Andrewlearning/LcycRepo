"""
给定一个不含重复单词的列表，编写一个程序，返回给定单词列表中所有的连接词。

连接词的定义为：一个字符串完全是由至少两个给定数组中的单词组成的。

示例:

输入: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

输出: ["catsdogcats","dogcatsdog","ratcatdogcat"]

解释: "catsdogcats"由"cats", "dog" 和 "cats"组成;
     "dogcatsdog"由"dog", "cats"和"dog"组成;
     "ratcatdogcat"由"rat", "cat", "dog"和"cat"组成。
"""

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # 去除重复的单词
        self.words = set(words)

        res = []

        # 检查每一个单词
        for word in words:
            if self.check(word):
                res.append(word)
        return res


    def check(self, word):

        length = len(word)

        # [0-i]前i个字母可以分解成最多多少个单词
        # 我们初始化前i个字母可以分解成负无穷的单词
        dp = [float("-inf") for i in range(len(word)+1)]

        # 前0个字母能分解成0个单词
        dp[0] = 0

        # [...i...j..length]
        # 主要看[..i) 和 [i..i+j)这两个能不能分别构成两个单词
        for i in range(length + 1):
            # 第二个单词的长度,i+j最长能到这个单词总长度
            for j in range(length-i, 0, -1):
                # 因为[..i]不能构成单词了，所以从[i+1..i+j)一个单词
                if dp[i] < 0:
                    continue

                # 假如[i..i+j)可以构成一个单词
                if word[i:i+j] in self.words:

                    # 那么从dp[0..i+j) 对进行一次更新
                    dp[i+j] = max(dp[i+j], dp[i] + 1)

                    # 当有答案满足的时候立刻返回TRUE
                    if dp[length] > 1:
                        return True

        return False

# https://www.acwing.com/video/1880/