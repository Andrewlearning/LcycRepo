"""
给定一组 互不相同 的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词
words[i] + words[j] ，可拼接成回文串。

示例 1：

输入：["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]]
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2：

输入：["bat","tab","cat"]
输出：[[0,1],[1,0]]
解释：可拼接成的回文串为 ["battab","tabbat"]
"""


import collections
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        inverse = collections.defaultdict(int)
        for i in range(len(words)):
            inverse[words[i][::-1]] = i

        res = []
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word) + 1):
                # 我们把一个单词以j为分界线分成左右两半
                left = word[0:j]
                right = word[j:]

                # 当结构是这样的  left right left[::-1]（这个单词是存在与words里的）, 他们可以形成回文的话
                # 首先检查right作为中间部分是不是回文的 self.check(right)
                # 然后看看left有没有相反顺序的串，假如说有的话，可以把相反串加在right右边
                # 当然，这个单词不能是自己,例如aa
                if self.check(right) and (left in inverse) and (inverse[left] != i):
                    res.append([i, inverse[left]])

                # 下面这个主体思路和上面的一样
                # len(word) != len(words[inverse[right]]) 这个表示的是
                # "abcd","dcba" 这种情况上面放进去过，下面有可能会再放一次
                # 所以我们就限定两个相同长度的单词的回文对组合只能被放进去一次
                if self.check(left) and (right in inverse) and (inverse[right] != i) and (
                        len(word) != len(words[inverse[right]])):
                    res.append([inverse[right], i])

        return res

    def check(self, word):
        l = 0
        r = len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True

# https://www.acwing.com/video/1727/