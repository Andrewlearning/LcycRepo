"""
给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。

word1 和 word2 是有可能相同的，并且它们将分别表示为列表中两个独立的单词。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"].

输入: word1 = “makes”, word2 = “coding”
输出: 1
输入: word1 = "makes", word2 = "makes"
输出: 3
"""
import sys
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not words:
            return None

        minDiff = sys.maxsize
        p1 = -1
        p2 = -1
        i = 0

        for i, word in enumerate(words):
            if word == word1:
                p1 = i
                if p1 != -1 and p2 != -1 and p1 != p2:
                    minDiff = min(minDiff, abs(p2 - p1))
            if word == word2:
                p2 = i
                if p1 != -1 and p2 != -1 and p1 != p2:
                    minDiff = min(minDiff, abs(p2 - p1))

        return minDiff