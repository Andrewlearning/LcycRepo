"""
给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。

题目保证至少有一个词不在禁用列表中，而且答案唯一。

禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。


"""
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")

        count = collections.Counter(
            word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans

"""
时间复杂度：O(P+B)，其中 PP 是段落 paragraph 的长度，BB 是禁用列表 banned 的长度。
空间复杂度：O(P+B)，用来进行计数以及存储禁用列表 banned。

https://leetcode-cn.com/problems/most-common-word/solution/zui-chang-jian-de-dan-ci-by-leetcode/
坑：
1. 首先我们得把字符串中的 !?',;. 给全部转换成空格
2. 然后把每个大写字母都转换成小写字母
3. 然后我们用split把字符串切割成数组
4. 最后统计词频，把没在ban的出现次数最多的单词选出来
"""