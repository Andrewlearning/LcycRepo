"""
Given p1 list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.
给定两个单词，问在列表里面这两个单词的最短距离是多少
"""
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        res = len(words)
        p1, p2 = -1, -1
        for i, word in enumerate(words):
            # 找到第一个单词的下标
            if word == word1:
                p1 = i
            # 找到第二个单词的下标
            if word == word2:
                p2 = i

            # 当两个单词的下标都找到的时候，我们可以计算它的下标差
            # 由于数组可能有重复，所以我们要不断地更新res
            if p1 != -1 and p2 != -1:
                res = min(res, abs(p1 - p2))

        return res

"""
时间复杂度：O(n)O 。这个问题的解法是线性的，我们无法比 O(n)更快是因为我们至少要遍历每个元素一次。
空间复杂度：O(1) 。没有使用额外空间。

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
给两个单词分配两个指针，当遍历到对应单词的时候，更新指针的值
然后当两个指针的值都更新过后，持续判断更新两指针的最小值
最后返回最小值
"""