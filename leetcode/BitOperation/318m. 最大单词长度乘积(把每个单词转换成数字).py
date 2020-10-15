"""
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "xtfn"。
示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。
"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        state = []
        for word in words:
            cur = 0
            # 一个数字有32位bit,我们可以用数字来记录26个字母，出现了哪个
            for char in word:
                cur |= 1 << (ord(char) - ord("a"))
            state.append(cur)

        res = 0
        for i in range(len(state) - 1):
            for j in range(i + 1, len(state)):
                # 假如两个单词 and 还是等于0，说明这两个单词没有字母相同
                if state[i] & state[j] == 0:
                    # 我们就可以来对比和更新长度了
                    res = max(res, len(words[i]) * len(words[j]))

        return res

# https://www.acwing.com/video/1706/