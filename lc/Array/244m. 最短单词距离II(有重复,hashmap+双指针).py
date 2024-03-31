"""
请设计一个类，使该类的构造函数能够接收一个单词列表。然后再实现一个方法，该方法能够分别接收两个单词 word1 和 word2，并返回列表中这两个单词之间的最短距离。您的方法将被以不同的参数调用 多次。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"]

输入: word1 = “coding”, word2 = “practice”
输出: 3
输入: word1 = "makes", word2 = "coding"
输出: 1

注意:
你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。
"""
import collections
class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.hashmap = collections.defaultdict(list)
        for i in range(len(words)):
            self.hashmap[words[i]].append(i)


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        loc1 = self.hashmap[word1]
        loc2 = self.hashmap[word2]
        p1 = 0
        p2 = 0
        diff = float("inf")

        while p1 < len(loc1) and p2 < len(loc2):
            diff = min(diff, abs(loc1[p1]-loc2[p2]))
            if loc1[p1] < loc2[p2]:
                p1 += 1
            else:
                p2 += 1


        return diff


# 链接：https://leetcode-cn.com/problems/shortest-word-distance-ii/solution/zui-duan-dan-ci-ju-chi-ii-by-leetcode/
