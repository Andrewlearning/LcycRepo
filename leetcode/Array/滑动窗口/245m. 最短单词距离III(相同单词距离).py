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
        
        diff = sys.maxsize
        p1 = -1
        p2 = -1
        i = 0

        while i < len(words):
            if words[i] == word1:
                p1 = i
                # 这个是用来检查word1,word2相等的情况
                # 因为经历第一个相同单词后，p1,p2下标相等
                # 但遇到第二个相同单词后，p1会率先更新，然后会更新diff
                if p2 != -1:
                    diff = min(diff, abs(p2 - p1))

            if words[i] == word2:
                p2 = i
                # 这个是用来更新正常word1,word2不相等的情况
                if p1 != -1 and p1 != p2:
                    diff = min(diff, abs(p2 - p1))

            # 下标更新
            i += 1
        
        return diff